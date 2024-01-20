import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


MIN_A = 1


def main():
    N = I()
    A = LI()
    D = I()
    L, R = [], []
    for _ in range(D):
        l, r = LI()
        L.append(l)
        R.append(r)

    cum_sum_from_left = calc_cum_sum_from_left(A, N)
    cum_sum_from_right = calc_cum_sum_from_right(A, N)

    sum_list = []
    for l, r in zip(L, R):
        sum_list.append(calc_sum(cum_sum_from_left, cum_sum_from_right, l, r))

    for s in sum_list:
        print(s)


def calc_sum(
    cum_sum_from_left: list[int], cum_sum_from_right: list[int], l: int, r: int
) -> int:
    left_max = cum_sum_from_left[l - 2] if l > 1 else MIN_A
    right_max = cum_sum_from_right[r]

    return max(left_max, right_max)


def calc_cum_sum_from_left(nums: list[int], size: int) -> list[int]:
    cum_sum = [0] * (size)
    max = MIN_A
    for i in range(size):
        if nums[i] > max:
            max = nums[i]
        cum_sum[i] = max

    return cum_sum


def calc_cum_sum_from_right(nums: list[int], size: int) -> list[int]:
    cum_sum = [0] * (size)
    max = MIN_A
    for i in range(size - 1, -1, -1):
        if nums[i] > max:
            max = nums[i]
        cum_sum[i] = max

    return cum_sum


if __name__ == "__main__":
    main()
