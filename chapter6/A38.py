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
    D, N = LI()
    L, R, H = [0], [0], [0]
    for _ in range(1, N + 1):
        l, r, h = LI()
        L.append(l)
        R.append(r)
        H.append(h)

    dp = [24] * (D + 1)
    dp[0] = 0

    for d in range(1, D + 1):
        for n in range(1, N + 1):
            if L[n] <= d <= R[n]:
                dp[d] = min(dp[d], H[n])

    print(sum(dp))


if __name__ == "__main__":
    main()
