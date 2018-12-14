from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import itertools

# calculate the frequencies of each informative word in the news
def getFrequency(words):
    sw = set(stopwords.words('english') + list(punctuation)) # stop words and punctuation
    freq = defaultdict(float) # store frequencies of each word
    count = 0
    for w in words:
        if w not in sw:
            freq[w] += 1 # appear times for w
            count += 1 # total number of words
    for w in freq:
        freq[w] = freq[w]/count # frequencies
    return freq

# find n senteces as the summary of the news
def findSummary(n, text):
    sentences = sent_tokenize(text) # divide the articles into sentences
    n = min(n, len(sentences))
    words = [word_tokenize(s.lower()) for s in sentences] # divide each sentence into words
    freq = getFrequency(list(itertools.chain.from_iterable(words)))
    score = defaultdict(float) # store score for each sentence i
    for i in range(len(words)):
        for w in words[i]:
            if w in freq:
                score[i] += freq[w]
    indices = nlargest(n, score, key=score.get) # get the indices of sentences with top n scores
    return [sentences[i] for i in indices]