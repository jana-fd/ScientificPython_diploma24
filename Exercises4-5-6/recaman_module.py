def recaman(N):
    seq = list()
    seq.append(0)
    for n in range(N):
        a = seq[n] - (n+1)
        if (a > 0) and (a not in seq):
            seq.append(a)
        else:
            seq.append(seq[n] + (n+1))
    return seq

def recaman1(N):
    exist = set()
    seq = list()
    n = 0
    a = 0
    while n <= N:
        diff = a - n
        if diff > 0 and diff not in exist:
            a = diff
        else:
            a = a + n
        exist.add(a)
        seq.append(a)
        n += 1
    return seq
