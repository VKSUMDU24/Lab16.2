import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

with open('text.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

words = word_tokenize(input_text)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in lemmatized_words if word.lower() not in stop_words]

filtered_words_no_punct = [word for word in filtered_words if word not in string.punctuation]
output_text = ' '.join(filtered_words_no_punct)

with open('outputtext.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(output_text)