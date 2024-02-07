import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


MAX_SIZE = 100
TRIANGLE_NUM = 3


def main():
    N = I()
    A = LI()

    num_counts = [0] * (MAX_SIZE + 1)

    for a in A:
        num_counts[a] += 1

    ans = 0
    for nc in num_counts:
        if nc < TRIANGLE_NUM:
            continue
        ans += calc_count(nc)

    print(ans)


def calc_count(n):
    return n * (n - 1) * (n - 2) // 6


if __name__ == "__main__":
    main()
