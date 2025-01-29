import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#nltk.download('stopwords')
#nltk.download('punkt_tab')

def word_frequency_without_stopwords(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.isalpha()] 
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    word_count = Counter(filtered_words)
    return word_count
file_path = 'Txtclassification.csv'
word_freq = word_frequency_without_stopwords(file_path)
wordcloud = WordCloud(width=900,height=500, max_words=1628,relative_scaling=1,normalize_plurals=False).generate_from_frequencies(word_freq)
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
