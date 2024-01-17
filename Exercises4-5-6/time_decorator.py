import time

def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print('Excution time: {} seconds.'.format(duration))
        return res
    return wrapper


@timer
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

@timer
def mt_sleep():
    time.sleep(2)

if __name__ == '__main__':
    re=recaman(1000)
    mt_sleep()
