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

    while True:
        count += 1

        time = find_earliest_end_time(current_time, L, R)

        if time == MAX_TIME:
            break

        current_time = time

    print(count)


# 最も早く終了する時間を見つける
def find_earliest_end_time(current_time: int, L: list, R: list) -> int:
    earliest_end_time = MAX_TIME
    for i in range(len(L)):
        if L[i] < current_time:
            continue
        earliest_end_time = min(earliest_end_time, R[i])
    return earliest_end_time


if __name__ == "__main__":
    main()
