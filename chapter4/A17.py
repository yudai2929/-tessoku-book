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

    # 動的計画法
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

    # 最短ルートから部屋を復元
    root = []
    place = N
    while place > 0:
        root.append(place)
        if dp[place - 2] + A[place - 1] == dp[place - 1]:
            place -= 1
        else:
            place -= 2

    root.reverse()
    print(len(root))
    print(*root)


if __name__ == "__main__":
    main()
