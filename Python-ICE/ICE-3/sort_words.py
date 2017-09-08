
# Function to sort list of words
def sortWords(maxLen):
    wordList = []
    while len(wordList) < int(maxLen):
        word = input("Enter word")
        wordList.append(word)
    wordList.sort()
    return wordList

inp=input("Enter the max number of words")
print(sortWords(inp))