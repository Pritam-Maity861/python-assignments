'''
12. Word Frequency Analyzer 
Given: 
text = """ 
Python is easy. 
Python is powerful. 
Python is widely used. 
""" 
Return: 
{ 
} 
"python": 3, 
"is": 3, 
"easy": 1, 
"powerful": 1, 
"widely": 1, 
"used": 1 
Create functions: 
get_word_frequency() 
get_most_common_word() 
get_unique_words() 
Handle 
● Empty input 
● Different capitalization 
● Punctuation 
'''

'''
class based Approach
'''

class WordFrequencyAnalyzer:
    def __init__(self, text):
        self.text = text

    def get_word_frequency(self):
        if not self.text.strip():
            return {}
        words = self.text.lower().split()
        word_frequency = {}
        for word in words:
            word = word.strip(".,!?;:")
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        return word_frequency

    def get_most_common_word(self):
        word_frequency = self.get_word_frequency()
        if not word_frequency:
            return None
        most_common = ""
        highest_count = 0
        for word in word_frequency:
            if word_frequency[word] > highest_count:
                highest_count = word_frequency[word]
                most_common = word

        return most_common

    def get_unique_words(self):
        word_frequency = self.get_word_frequency()
        return list(word_frequency.keys())


text = """
Python is easy.
Python is powerful.
Python is widely used.
"""

analyzer = WordFrequencyAnalyzer(text)

print("Word Frequency:")
print(analyzer.get_word_frequency())

print("Most Common Word:")
print(analyzer.get_most_common_word())

print("Unique Words:")
print(analyzer.get_unique_words())
