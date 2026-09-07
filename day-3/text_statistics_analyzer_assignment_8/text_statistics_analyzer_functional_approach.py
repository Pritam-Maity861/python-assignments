text = """
Python is powerful.
Python is simple.
Python is popular.
"""

def number_of_characters(text):
    return len(text)

def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_sentences(text):
    sentences = text.split(".")
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(sentences)

def number_of_unique_words(text):
    words = text.lower().split()
    clean_words = []
    for word in words:
        word = word.strip(".,!?")
        clean_words.append(word)

    return len(set(clean_words))

def most_frequent_word(text):
    words = text.lower().split()
    clean_words = []
    for word in words:
        word = word.strip(".,!?")
        clean_words.append(word)

    word_count = {}
    for word in clean_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_common = ""
    highest_count = 0

    for word in word_count:
        if word_count[word] > highest_count:
            highest_count = word_count[word]
            most_common = word

    return most_common


def longest_word(text):
    words = text.lower().split()
    clean_words= []
    for word in words:
        word =word.strip(".,!?")
        clean_words.append(word)

    return max(clean_words, key=len)


def shortest_word(text):
    words = text.lower().split()
    clean_words=[]
    for word in words:
        word=word.strip(".,!?")
        clean_words.append(word)

    return min(clean_words, key=len)


print("number of characters : ", number_of_characters(text))
print("number of words:", number_of_words(text))
print("number of sentences:", number_of_sentences(text))
print("number of unique words:", number_of_unique_words(text))
print("most frequent word:", most_frequent_word(text))
print("longest word:", longest_word(text))
print("shortest word:", shortest_word(text))
