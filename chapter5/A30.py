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
    n, r = LI()

    n_fact = calc_factorial_mod(n, DIVIDED_NUMBER)
    r_fact = calc_factorial_mod(r, DIVIDED_NUMBER)
    nr_fact = calc_factorial_mod(n - r, DIVIDED_NUMBER)

    print(
        n_fact
        * power(r_fact, DIVIDED_NUMBER - 2, DIVIDED_NUMBER)
        * power(nr_fact, DIVIDED_NUMBER - 2, DIVIDED_NUMBER)
        % DIVIDED_NUMBER
    )


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


def calc_factorial_mod(n: int, m: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result = result * i % m
    return result


if __name__ == "__main__":
    main()
