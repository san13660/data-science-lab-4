from nltk.util import ngrams
from nltk.corpus import gutenberg

gut_ngrams = ( ngram for sent in gutenberg.sents() for ngram in ngrams(sent, 3, pad_left = True, pad_right = True, right_pad_symbol='EOS', left_pad_symbol="BOS"))
freq_dist = nltk.FreqDist(gut_ngrams)
kneser_ney = nltk.KneserNeyProbDist(freq_dist)

prob_sum = 0
for i in kneser_ney.samples():
    if i[0] == "I" and i[1] == "confess":
        prob_sum += kneser_ney.prob(i)
        print("{0}:{1}".format(i, kneser_ney.prob(i)))
print(prob_sum)