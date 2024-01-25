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
    N, W = LI()
    U, V = [], []
    for _ in range(N):
        w, v = LI()
        U.append(w)
        V.append(v)

    dp = [[-1 for _ in range(W + 1)] for _ in range(N + 1)]

    dp[0][0] = 0
    for i in range(N):
        for j in range(W + 1):
            if j >= U[i]:
                dp[i + 1][j] = max(dp[i][j - U[i]] + V[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]

    print(max(dp[N]))


if __name__ == "__main__":
    main()
