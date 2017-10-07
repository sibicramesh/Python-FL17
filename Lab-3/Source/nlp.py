from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
import nltk


# Function to Tokenize the input text
def Tokenize(text):
    tokens = word_tokenize(text)
    print '******** Tokenize *********'
    print tokens, '\n'
    return tokens


# Function to remove stop words
def StopWordsRemoval(tokens):
    stopWords = stopwords.words('english')
    filteredWords = [wo for wo in tokens if wo not in stopWords]
    wordsWithoutStops = [wo for wo in filteredWords if len(wo) > 2]
    print '******** Filtered Words *********'
    print wordsWithoutStops, '\n'
    return wordsWithoutStops


# Function to Lemmatize
def Lemmatizer(nonstop):
    resultList = list()
    for j in nonstop:
        resultList.append(WordNetLemmatizer().lemmatize(j))
    print '******** Lemmatized Words *********'
    print resultList, '\n'
    return resultList


# Function to remove verbs
def RemoveVerbs(lemwords):
    resultList = list()
    for j in pos_tag(lemwords):
        if j[1][:2] == 'VB':
            continue
        else:
            resultList.append(j[0])
    print '******** Verb Removal *********'
    print resultList, '\n'
    return resultList


# Function to calculate word frequency
def WordFrequenxy(verbless):
    wordsFreq = nltk.FreqDist(verbless)
    topFive = dict()
    for w, f in wordsFreq.most_common(5):
        topFive[w] = f
    print '******** Top Five Keys and Values *********'
    print topFive, '\n'
    return topFive


# Function to get just top five words
def GetWords(topfive):
    topFiveWords = topfive.keys()
    print '******** Top Five Words *********'
    print topFiveWords, '\n'
    return topFiveWords


# Function to find sentences with top five words
def FindSentences(text, topfive):
    result = list()
    for l in text.split('\n'):
        for w in topfive:
            if w in l.lower():
                result.append(l)
                break
    return result


# Function to summarize
def Summarizer(sentences):
    print '******** Summary *********'
    print '\n'.join(sentences)


def main():
    text = open('/Volumes/Sibi-CLG/PythonFall17/Python-FL17/Lab-3/Source/data/input.txt', "r").read()
    tokens = Tokenize(text)
    nonstop = StopWordsRemoval(tokens)
    lemwords = Lemmatizer(nonstop)
    verbless = RemoveVerbs(lemwords)
    topfive = WordFrequenxy(verbless)
    topfivewords = GetWords(topfive)
    sentences = FindSentences(text, topfivewords)
    Summarizer(sentences)


if __name__ == "__main__":
    main()
