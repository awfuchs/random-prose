# Random prose generator.
# Nicer output with fold -s so on Linux invoke it like this:
#
#   python rant.py | fold -s

import re
import random

numSentences=50

# Just move the one you want to the last position...
source='texts/andersen.txt'
source='texts/christie.txt'
source='texts/donneepoeti.txt'
source='texts/federalist.txt'
source='texts/googley.txt'
source='texts/kjbible.txt'
source='texts/kjgenesis.txt'
source='texts/sciam.txt'
source='texts/technical.txt'

# You'll probably want to tune these weightings depending on the text selected
sentRunonWeighting=5
paraBloatWeighting=7

print
print
print

# Input a list of sentences
f = open(source, 'r')
theText = ' '.join(f.readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', theText)

# Set up containers
firstWords=[]
lastWords=[]
wordPairs={}
wordTriples={}

# ====== Loop through sentences, building start, end, and transition word lists =====
for s in sentences:
  words=s.split()
  if len(words)>2:
    # --- Add first and last sentence words to respective lists ---
    firstWords.append(words[0])
    lastWords.append(words[-1])
    # --- Populate dictionary of w1->w2 transitions ---
    w=words[0]
    n=words[1]
    if w not in wordPairs:     # If the key doesn't exist yet...
      wordPairs.update({w:[]}) # ...then add it
    # --- Accumulate ->w2 transitions for each w1-> ---
    wordPairs[w].append(n)
    # --- Now loop through and build triples dictionary ---
    for i in range(len(words)-2):
      w1=words[i]
      w2=words[i+1]
      n=words[i+2]
      if (w1,w2) not in wordTriples:     # If the double key doesn't exist yet...
        wordTriples.update({(w1,w2):[]}) # ...then add it
      # --- Accumulate ->w3 transitions for each w1->w2-> ---
      wordTriples[w1,w2].append(n)


# ======= Output a constructed sequence of words =========
for c in range(numSentences):
  wcount=0
  w1=firstWords[random.randint(0,len(firstWords))-1] # Pick a w1->
  w2=random.choice(wordPairs[w1]) # and one of its possible ->w2
  print w1, w2, # Output these first two words
  wcount+=2
  while True:
    nextword=random.choice(wordTriples[w1,w2]) # pick a ->w3
    # --- Should we end the sentence at this word? ---
    if (nextword in lastWords and random.randint(0,sentRunonWeighting-wcount)<=0) or (w2,nextword) not in wordTriples:
      print nextword+".",
      # --- Should we insert a paragraph break? ---
      if random.randint(0,paraBloatWeighting)==0:
        print
        print
      break
    else:
      print nextword,
      w1=w2
      w2=nextword

print
print
print
# print lastWords
