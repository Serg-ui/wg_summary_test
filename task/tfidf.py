from collections import Counter
from math import log10
import operator


def get_words(data, many=False) -> list:
    words = []
    to_clear = ',.!?:;*()"'

    if many:
        words_tmp = []

        for d in data:
            for word in d.split():
                words_tmp.append(word.strip(to_clear).lower())

            words.append(words_tmp)

        return words

    for word in data.split():
        words.append(word.strip(to_clear).lower())

    return words


def get_tfidf(main, others):
    for word, value in main.items():
        nz = sum([1.0 for i in others if word in i]) or 1
        idf = log10(len(others) / nz)

        value.append(value[1] * idf)

    res = sorted(main.items(), key=lambda item: item[1][2], reverse=True)
    return res
