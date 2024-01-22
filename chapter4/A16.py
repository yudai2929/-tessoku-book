import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()
    A = LI()
    B = LI()

    A.insert(0, 0)
    B.insert(0, 0)
    B.insert(1, 0)

    dp = []

    for i in range(N):
        if i == 0:
            dp.append(0)
            continue

        if i == 1:
            dp.append(A[i])
            continue

        a = dp[i - 1] + A[i]
        b = dp[i - 2] + B[i]
        dp.append(min(a, b))

    print(dp[-1])


if __name__ == "__main__":
    main()
