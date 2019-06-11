import random
import string

def make_histogram(s):
    """Make a map from letters to number of times they appear in s.

    s: string

    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    for c in string.whitespace + string.punctuation:
        if c in hist:
            hist.pop(c)
    return hist


def random_choice(hist):
    t = []
    for x, freq in hist.items():
        for i in range(freq):
            t.append((freq, x))
    t.sort(reverse=True)
    a = random.choice(t)
    return a


def distribution_tester(hist, n):
    d = dict()
    for i in range(n):
        res = random_choice(hist)
        d[res] = d.get(res, 0) + 1
    print(d)


if __name__ == '__main__':
    s = "i aaaa bb"
    histogram = make_histogram(s)
    distribution_tester(histogram, 10000)