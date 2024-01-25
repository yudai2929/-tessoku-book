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
    N, S = LI()
    A = LI()

    dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]

    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j >= A[i]:
                dp[i + 1][j] = dp[i][j - A[i]] or dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j]

    if dp[N][S]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
