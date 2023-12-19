# Import necessary libraries
import spacy
from spacy.lang.en import English
from spacy.pipeline.textcat import Config, single_label_cnn_config
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = English()

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

# Create a text classification model using spaCy
text_cat_config = Config().from_str(single_label_cnn_config)
text_cat_config['exclusive_classes'] = True

text_classifier = text_cat_config['model'](text_cat_config)
text_classifier.add_label("Theft")
text_classifier.add_label("Assault")
# Add more labels for different FIR categories

# Train the text classification model
train_data = list(zip(train_texts, [{'cats': {label: label == true_label for label in text_classifier.labels}} for true_label in train_labels]))
text_classifier.update(train_data, drop=0.5, losses={})

# Test the text classification model
test_data = list(zip(test_texts, test_labels))
predictions = [text_classifier(text) for text, _ in test_data]
predicted_labels = [max(prediction.cats, key=prediction.cats.get) for prediction in predictions]

# Evaluate the model
accuracy = accuracy_score(test_labels, predicted_labels)
print(f"Accuracy: {accuracy}")

# Now you can integrate this with the FIR generation and structuring components based on your specific requirements.