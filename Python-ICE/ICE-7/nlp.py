from nltk import pos_tag, ne_chunk, word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer


def FindMeanings(s):
    from nltk.corpus import wordnet as wn
    l = s.split()
    synsets = wn.synsets(l[2])
    print '******** WordNet *********'
    print[str(syns.definition) for syns in synsets], '\n'


def Tokenize(s):
    print '******** Tokenize *********'
    print sent_tokenize(s), '\n'


def Stem(s):
    stems = PorterStemmer()
    w = s.split()
    print '******** Stemming *********'
    print stems.stem(w[12]), '\n'


def FindPOS(s):
    from nltk.tag import pos_tag
    w = word_tokenize(s)
    print '******** POS *********'
    print pos_tag(w), '\n'


def Lemmatize(s):
    wl = WordNetLemmatizer()
    w = s.split()
    print '******** Lemmatize *********'
    print wl.lemmatize(w[12], pos='v'), '\n'


def Trigram(s):
    from  nltk.util import ngrams
    tk = word_tokenize(s.lower())
    print '******** Trigram *********'
    for i in ngrams(tk, 3):
        print i
    print '\n'


def EntityRecognizer(s):
    print '******** EntityRecognizer *********'
    print ne_chunk(pos_tag(wordpunct_tokenize(s)))


print '******* NLP ******'
text = open("input.txt", "r").read()

FindMeanings(text)
Tokenize(text)
Stem(text)
FindPOS(text)
Lemmatize(text)
Trigram(text)
EntityRecognizer(text)
