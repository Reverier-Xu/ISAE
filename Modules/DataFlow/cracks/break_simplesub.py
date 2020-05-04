from ..pycipher.simplesubstitution import SimpleSubstitution as SimpleSub
import random
import re
from .ngram_score import ngram_score

fitness = ngram_score('Modules/DataFlow/cracks/quadgrams.txt') # load our quadgram statistics
def break_simplesub(ctext):
    ctext = re.sub('[^A-Z]','',ctext.upper())

    maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    maxscore = -99e9
    parentscore,parentkey = maxscore,maxkey[:]

    # keep going until we are killed by the user
    i = 0
    out = ''
    for i in range(200):
        print(i)
        random.shuffle(parentkey)
        deciphered = SimpleSub(parentkey).decipher(ctext)
        parentscore = fitness.score(deciphered)
        count = 0
        while count < 1000:
            a = random.randint(0,25)
            b = random.randint(0,25)
            child = parentkey[:]
            # swap two characters in the child
            child[a],child[b] = child[b],child[a]
            deciphered = SimpleSub(child).decipher(ctext)
            score = fitness.score(deciphered)
            # if the child was better, replace the parent with it
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count + 1
        # keep track of best score seen so far
        if parentscore > maxscore:
            maxscore,maxkey = parentscore,parentkey[:]
            temp = '\nbest score so far: '+str(maxscore)+' on iteration '+str(i)
            ss = SimpleSub(maxkey)
            temp+= '    best key: '+''.join(maxkey)
            temp += '    plaintext: ' + ss.decipher(ctext)
            out = temp + out
    print(out)
    return out
