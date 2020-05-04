# this code cracks the affine cipher
import re
from .ngram_score import ngram_score
from ..pycipher.affine import Affine


fitness = ngram_score('Modules/DataFlow/cracks/quadgrams.txt')  # load our quadgram statistics

def break_affine(ctext):
    def break_(text):
        # make sure ciphertext has all spacing/punc removed and is uppercase
        text = re.sub('[^A-Z]','',text.upper())
        # try all posiible keys, return the one with the highest fitness
        scores = []
        for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
            scores.extend([(fitness.score(Affine(i,j).decipher(text)),(i,j)) for j in range(0,25)])
        return max(scores)
    max_key = break_(ctext)
    return 'best candidate with key (a,b) = '+str(max_key[1])+':'+ '\n'+Affine(max_key[1][0],max_key[1][1]).decipher(ctext)
