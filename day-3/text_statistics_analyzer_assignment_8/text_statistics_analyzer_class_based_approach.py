class TextStatisticsAnalyzer:
    def __init__(self, text):
        self.text=text

    def number_of_characters(self):
        return len(self.text)

    def number_of_words(self):
        words=self.text.split()
        return len(words)

    def number_of_sentences(self):
        sentences=self.text.split(".")
        sentences=[sentence for sentence in sentences if sentence.strip()]
        return len(sentences)

    def number_of_unique_words(self):
        words=self.text.lower().split()
        clean_words = []
        for word in words:
            word=word.strip(".,!?")
            clean_words.append(word)

        return len(set(clean_words))

    def most_frequent_word(self):
        words = self.text.lower().split()
        clean_words = []
        for word in words:
            word= word.strip(".,!?")
            clean_words.append(word)

        word_count= {}
        for word in clean_words:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1

        most_common=""
        highest_count=0
        for word in word_count:
            if word_count[word] > highest_count:
                highest_count=word_count[word]
                most_common=word

        return most_common

    def longest_word(self):
        words = self.text.lower().split()
        clean_words = []
        for word in words:
            word= word.strip(".,!?")
            clean_words.append(word)

        return max(clean_words, key=len)

    def shortest_word(self):
        words=self.text.lower().split()
        clean_words= []
        for word in words:
            word=word.strip(".,!?")
            clean_words.append(word)

        return min(clean_words, key=len)



text = """
Python is powerful.
Python is simple.
Python is popular.
"""

analyzer = TextStatisticsAnalyzer(text)

print("number of characters:", analyzer.number_of_characters())
print("number of words:", analyzer.number_of_words())
print("number of sentences:", analyzer.number_of_sentences())
print("number of unique words:", analyzer.number_of_unique_words())
print("most frequent word:", analyzer.most_frequent_word())
print("longest word:", analyzer.longest_word())
print("shortest word:", analyzer.shortest_word())
