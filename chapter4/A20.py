import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def Str():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def main():
    S = Str()
    T = Str()

    dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]

    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] == T[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    print(dp[len(S)][len(T)])


if __name__ == "__main__":
    main()
