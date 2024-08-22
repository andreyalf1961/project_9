from itertools import combinations


def all_variants(text):
    for c in range(1, len(text) + 1):
        comb = combinations(text, c)
        for t in comb:
            t = ''.join(t)
            yield t


txt = 'abcd'
a = all_variants(txt)
for i in a:
    if len(i) == 1:
        print(i)
    else:
        for j in range(1, len(i)):
            a_1 = txt.index(i[j - 1])
            a_2 = txt.index(i[j])
            if a_2 - a_1 > 1:
                break
            if j == len(i) - 1:
                print(i)
