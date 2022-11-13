import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

class Tokenizador():

    def __init__(self, text) -> None:
        print(text)
        self.lemmatizer = WordNetLemmatizer()
        self.ps = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
    def tokenizer(self, text):
        print('ENTRÓ')
        text = text.replace("\n", " ")
        tokens = word_tokenize(text)
        tokens = [t for t in tokens if t.isalpha()]
        tokens = [self.lemmatizer.lemmatize(t) for t in tokens]
        tokens = [self.ps.stem(t) for t in tokens]
        tokens = [t for t in tokens if len(t) > 2]
        print('SALIÓ')
        return tokens