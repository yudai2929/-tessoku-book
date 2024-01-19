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
    H, W = LI()
    X = []
    for _ in range(H):
        X.append(LI())
    Q = I()
    A, B, C, D = [], [], [], []
    for _ in range(Q):
        a, b, c, d = LI()
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    cum_sum_matrix = calc_cum_sum_matrix(X, H, W)

    sum_list = []
    for a, b, c, d in zip(A, B, C, D):
        sum_list.append(calc_sum(cum_sum_matrix, a, b, c, d))

    for s in sum_list:
        print(s)


def calc_sum(cum_sum_matrix: list[list[int]], a: int, b: int, c: int, d: int) -> int:
    if a == 1 and b == 1:
        return cum_sum_matrix[c - 1][d - 1]
    elif a == 1:
        return cum_sum_matrix[c - 1][d - 1] - cum_sum_matrix[c - 1][b - 2]
    elif b == 1:
        return cum_sum_matrix[c - 1][d - 1] - cum_sum_matrix[a - 2][d - 1]
    else:
        return (
            cum_sum_matrix[c - 1][d - 1]
            - cum_sum_matrix[c - 1][b - 2]
            - cum_sum_matrix[a - 2][d - 1]
            + cum_sum_matrix[a - 2][b - 2]
        )


def calc_cum_sum(nums: list[int], size: int) -> list[int]:
    cum_sum = [0] * (size)
    for i in range(size):
        if i == 0:
            cum_sum[i] = nums[i]
            continue
        cum_sum[i] = cum_sum[i - 1] + nums[i]

    return cum_sum


def calc_cum_sum_matrix(matrix: list[list[int]], h: int, w: int) -> list[list[int]]:
    h_cum_sum_matrix = []

    # h方向の累積和を計算
    for i in range(h):
        h_cum_sum_matrix.append(calc_cum_sum(matrix[i], w))

    cum_sum_matrix = [[0] * w for _ in range(h)]
    # w方向の累積和を計算
    for i in range(h):
        for j in range(w):
            if i == 0:
                cum_sum_matrix[i][j] = h_cum_sum_matrix[i][j]
                continue
            cum_sum_matrix[i][j] = cum_sum_matrix[i - 1][j] + h_cum_sum_matrix[i][j]

    return cum_sum_matrix


if __name__ == "__main__":
    main()
