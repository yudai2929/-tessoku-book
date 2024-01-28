import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


DIVIDED_NUMBER = 10**9 + 7


def main():
    a, b = LI()

    print(power(a, b, DIVIDED_NUMBER))


def power(a: int, b: int, m: int) -> int:
    p = a
    result = 1
    while b > 0:
        # bの最下位ビットが1のとき. 2進数で表すと, 1の位が1のとき. 2で割るときの余りが1のとき.
        if b & 1:
            result = result * p % m
        p = p * p % m
        b >>= 1
    return result


if __name__ == "__main__":
    main()
