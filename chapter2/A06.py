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
    N, Q = LI()
    A = LI()
    L, R = [], []
    for _ in range(Q):
        l, r = LI()
        L.append(l)
        R.append(r)

    cum_sum = calc_cum_sum(A, N)

    sum_list = []
    for l, r in zip(L, R):
        sum_list.append(calc_sum(cum_sum, l, r))

    for s in sum_list:
        print(s)


def calc_cum_sum(nums: list[int], size: int) -> list[int]:
    cum_sum = [0] * (size)
    for i in range(size):
        if i == 0:
            cum_sum[i] = nums[i]
            continue

        cum_sum[i] = cum_sum[i - 1] + nums[i]

    return cum_sum


def calc_sum(cum_sum: list[int], l: int, r: int) -> int:
    if l == 1:
        return cum_sum[r - 1]
    return cum_sum[r - 1] - cum_sum[l - 1 - 1]


if __name__ == "__main__":
    main()
