# Import necessary libraries
import spacy
from spacy.training.example import Example
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.blank("en")

# Sample data for training the text classification model
data = [
    ("Complaint about theft. Occurred at 123 Main St. on 2023-01-15.", "Theft"),
    ("Assault reported at 456 Oak St. on 2023-02-20.", "Assault"),
    # Add more data with different categories
]

# Split data into training and testing sets
train_texts, test_texts, train_labels, test_labels = train_test_split(
    [text for text, label in data],
    [label for text, label in data],
    test_size=0.2
)

# Create a TextCategorizer instance
text_cat = nlp.add_pipe("textcat")
text_cat.add_label("Theft")
text_cat.add_label("Assault")
# Add more labels for different FIR categories

# Prepare training data
train_data = list(zip(train_texts, [{'cats': {label: label == true_label for label in text_cat.labels}} for true_label in train_labels]))
train_examples = []
for text, annotation in train_data:
    example = Example.from_dict(nlp.make_doc(text), annotation)
    train_examples.append(example)

# Train the text classification model using spacy.cli.train
train_config = {"textcat": {"exclusive_classes": True, "architecture": "simple_cnn"}}
spacy.cli.train(nlp, train_examples, output_dir="output", train_cfg=train_config)

# Test the text classification model
test_data = list(zip(test_texts, test_labels))
predicted_labels = []
for text, true_label in test_data:
    doc = nlp(text)
    predicted_label = max(doc.cats, key=doc.cats.get)
    predicted_labels.append(predicted_label)

# Evaluate the model
accuracy = accuracy_score(test_labels, predicted_labels)
print(f"Accuracy: {accuracy}")
