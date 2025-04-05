from flask import Flask, request, render_template
from joblib import load
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

clf = load("model1.joblib")
vectorizer = load("vectorizer1.joblib")

def preprocess_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove punctuation and digits
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))

    # Tokenize the text
    words = word_tokenize(text)

    # Remove stop words
    words = [word for word in words if word not in stop_words]

    # Stem or lemmatize the words
    words = [stemmer.stem(word) for word in words]

    # Join the words back into a string
    text = ' '.join(words)

    return text


app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/a')
def about_us():
    return render_template('aboutus.html')
@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    preprocessed_text = preprocess_text(text)
    X = vectorizer.transform([preprocessed_text])
    y_pred = clf.predict(X)
    if y_pred[0]== 1:
        result = 'Real'
    else:
        result = 'Fake'
    return render_template('result.html', result=result, text=text)

if __name__ == '__main__':
    app.run(debug=True)
