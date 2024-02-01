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

    dp = [[0] * (N) for _ in range(N)]

    dp[N - 1] = A

    for i in range(N - 2, -1, -1):
        for j in range(1, i + 2):
            if i % 2 == 0:
                dp[i][j - 1] = max(dp[i + 1][j], dp[i + 1][j - 1])
            else:
                dp[i][j - 1] = min(dp[i + 1][j], dp[i + 1][j - 1])

    print(dp[0][0])


if __name__ == "__main__":
    main()
