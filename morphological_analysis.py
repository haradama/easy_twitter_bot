#coding: utf-8

from janome.tokenizer import Tokenizer
from collections import Counter

t = Tokenizer()

with open("tweets.txt", "r") as f:
    words = []
    for line in f:
        l = line.rstrip()
        tokens = t.tokenize(l)

        for token in tokens:
            part = token.part_of_speech.split(',')[0]
            if part == "名詞":
                word = token.surface
                words.append(word)

counter = Counter(words)

with open("word_frequency.txt", "w") as f:
    for word, cnt in counter.most_common():
        f.write("{0}\t{1}\n".format(word, cnt))
