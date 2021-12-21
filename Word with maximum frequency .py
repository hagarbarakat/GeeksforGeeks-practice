from collections import OrderedDict


def maximumFrequency(S):
    hashmap = OrderedDict()
    w, frequency = "", 0
    sentence = S.split()
    for word in sentence:
        if word in hashmap:
            hashmap[word] += 1
        else:
            hashmap[word] = 1

    for k, v in hashmap.items():
        if hashmap[k] > frequency:
            frequency = hashmap[k]
            w = k
    return w + " " + str(frequency)
