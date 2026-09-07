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
Functional Approach
'''

def get_word_frequency(text):
    if not text.strip():
        return {}
    words = text.lower().split()
    word_frequency = {}
    for word in words:
        word = word.strip(".,!?;:")
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency


def get_most_common_word(text):
    word_frequency = get_word_frequency(text)
    if not word_frequency:
        return None
    most_common = ""
    highest_count = 0
    for word in word_frequency:
        if word_frequency[word] > highest_count:
            highest_count = word_frequency[word]
            most_common = word
    return most_common


def get_unique_words(text):
    word_frequency = get_word_frequency(text)
    return list(word_frequency.keys())


text = """
Python is easy.
Python is powerful.
Python is widely used.
"""

print("Word Frequency:")
print(get_word_frequency(text))

print("Most Common Word:")
print(get_most_common_word(text))

print("Unique Words:")
print(get_unique_words(text))
