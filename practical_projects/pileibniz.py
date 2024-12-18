"""Try to calculate pi."""
import time
menet = 10000000


def main():
    """Calculate pi."""
    n = menet
    pi = 4 * sum(1 / i for i in range(1-2*n, 2*n+1, 4))
    print("{:.32f}".format(pi))


ktime = time.time()
main()
print(f'--- {time.time() - ktime} másodperc.')