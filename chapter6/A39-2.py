import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


MAX_TIME = 86400


def main():
    N = I()
    L, R = [], []
    for _ in range(N):
        l, r = LI()
        L.append(l)
        R.append(r)

    current_time = 0
    count = 0

    sort_by_end_time(L, R)

    for i in range(N):
        if L[i] < current_time:
            continue
        current_time = R[i]
        count += 1

    print(count)


# 終了時間が最も早いもの順にソートする
def sort_by_end_time(L: list, R: list) -> None:
    # Create a list of tuples from L and R
    LR = list(zip(L, R))

    # Sort the list of tuples based on the second element of each tuple
    LR.sort(key=lambda x: x[1])

    # Unzip the list of tuples back into L and R
    L, R = zip(*LR)


if __name__ == "__main__":
    main()
