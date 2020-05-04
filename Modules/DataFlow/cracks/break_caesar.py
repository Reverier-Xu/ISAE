import re
from .ngram_score import ngram_score
fitness = ngram_score('Modules/DataFlow/cracks/quadgrams.txt') # load our quadgram statistics
from ..pycipher.caesar import Caesar
def break_caesar(ctext):

    def break_(text):
        # make sure ciphertext has all spacing/punc removed and is uppercase
        text = re.sub('[^A-Z]','',text.upper())
        # try all possible keys, return the one with the highest fitness
        scores = []
        for i in range(26):
            scores.append((fitness.score(Caesar(i).decipher(text)),i))
        return max(scores)

    # example ciphertext
    max_key = break_(ctext)

    out = 'best candidate with key (a,b) = '+str(max_key[1])+':\n'
    out += Caesar(max_key[1]).decipher(ctext)
    return out
