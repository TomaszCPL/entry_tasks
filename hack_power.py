import re
import collections
from collections import Counter

#REMARKS!!! I wasn't sure if it is the right way the input should look like.
#However it can be very easily changed.
#Right now It can work for any given dict of letters.
#However, the way it is constructed for phrases(in order to avoid overlapping) is to sort it by the length of a key.
#So it can meet some problems if there is no direct relationship between length of phrases and their value.

def passwordCalculator(password):
    letters = {"a":1,"b":2,"c":3}
    for letter in list(password):
        if letter not in letters:
            return ("Invalid hack")
        
    phrases = {"baa": 20, "ba": 10}
    hackPower = 0
    counter = Counter(list(password))
    for letter in counter.keys():
        if letter in letters.keys():
            hackPower += sum([letters.get(letter) * i for i in range(1,counter.get(letter)+1)])

    sortedPhrases = collections.OrderedDict(sorted(phrases.items(),key=lambda t: t[0],reverse=True))
    regex = '|'.join(re.escape(phrase) for phrase in sortedPhrases)
    hackPower += sum(phrases[match] for match in re.findall(regex, password))

    return hackPower
