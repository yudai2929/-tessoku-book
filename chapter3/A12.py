import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


MAX_TIME = 10**9


def main():
    N, K = LI()
    A = LI()

    time = find_time_by_bin_search(A, K)
    print(time)


def find_time_by_bin_search(A: list[int], K: int) -> int:
    left = 1
    right = MAX_TIME

    while left <= right:
        mid = (left + right) // 2

        if check(mid, K, A):
            right = mid - 1
        else:
            left = mid + 1

    return left


def check(time: int, K: int, A: list[int]) -> bool:
    count = 0
    for a in A:
        count += time // a

    return count >= K


if __name__ == "__main__":
    main()
