import re
import nltk
from collections import Counter
from nltk.corpus import stopwords

def remove_stopwords(text):

    nltk.download('stopwords')
    
    stop_words = set(stopwords.words('english'))
    
    words = re.findall(r'\b\w+\b', text.lower())
    
    filtered_words=[]
    for word in words:
        if not(word in stop_words):
            filtered_words.append(word)

    return filtered_words

def count_word_frequency(words):
    word_counts = Counter(words)
    return word_counts

def main():
    text = open("C:\\Users\\mazen ayman\\Documents\\random_paragraphs.txt").read()
    processed_text = remove_stopwords(text)
    
    word_counts = count_word_frequency(processed_text)
    
    print("Word Frequency Count:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")


main()