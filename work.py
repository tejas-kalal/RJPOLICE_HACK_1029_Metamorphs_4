import nltk
from textblob import TextBlob

# Download specific NLTK data
nltk.download('punkt', download_dir='C:\\Users\\tejas\\Desktop\\Computer Langauges\\Rajasthan_police_Hackthon\\nltk_data')
nltk.download('averaged_perceptron_tagger', download_dir='C:\\Users\\tejas\\Desktop\\Computer Langauges\\Rajasthan_police_Hackthon\\nltk_data')

# Specify the local path for NLTK data
nltk.data.path.append('C:\\Users\\tejas\\Desktop\\Computer Langauges\\Rajasthan_police_Hackthon\\nltk_data')

# Sample complainant-provided information
complaint_text = "I witnessed a theft near my house. The suspect was wearing a black hoodie and ran away."

# Tokenization and POS tagging using NLTK
def extract_entities(text):
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    entities = {tag: word for word, tag in pos_tags}
    return entities

entities = extract_entities(complaint_text)
print("Entities:", entities)

# Sentiment analysis using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_scores = {'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity}
    return sentiment_scores

sentiment_scores = analyze_sentiment(complaint_text)
print("Sentiment Scores:", sentiment_scores)

