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
    D = I()
    N = I()

    L, R = [], []
    for _ in range(N):
        l, r = LI()
        L.append(l)
        R.append(r)

    diff_list = [0] * D
    for l, r in zip(L, R):
        diff_list = calc_diff_list(diff_list, l, r)

    cum_sum = calc_cum_sum(diff_list, D)

    for cs in cum_sum:
        print(cs)


def calc_diff_list(mut_diff_list: list[int], l: int, r: int) -> list[int]:
    mut_diff_list[l - 1] += 1
    if r < len(mut_diff_list):
        mut_diff_list[r] -= 1

    return mut_diff_list


def calc_cum_sum(nums: list[int], size: int) -> list[int]:
    cum_sum = [0] * (size)
    for i in range(size):
        if i == 0:
            cum_sum[i] = nums[i]
            continue

        cum_sum[i] = cum_sum[i - 1] + nums[i]

    return cum_sum


if __name__ == "__main__":
    main()
