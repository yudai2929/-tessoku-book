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
    H, W, N = LI()
    A, B, C, D = [], [], [], []
    for _ in range(N):
        a, b, c, d = LI()
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    matrix = generate_matrix(H, W)
    for a, b, c, d in zip(A, B, C, D):
        matrix = stack_sone(matrix, a, b, c, d)

    cum_sum_matrix = calc_cum_sum_matrix(matrix, H, W)

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            print(cum_sum_matrix[i][j], end=" ")
        print()


def stack_sone(
    matrix: list[list[int]],
    a: int,
    b: int,
    c: int,
    d: int,
) -> list[list[int]]:
    cp_matrix = matrix.copy()
    cp_matrix[a][b] += 1
    cp_matrix[a][d + 1] -= 1
    cp_matrix[c + 1][b] -= 1
    cp_matrix[c + 1][d + 1] += 1
    return cp_matrix


def calc_cum_sum_matrix(matrix: list[list[int]], h: int, w: int) -> list[list[int]]:
    h_cum_sum_matrix = generate_matrix(h, w)
    # h方向の累積和を計算
    for i in range(h):
        for j in range(w):
            h_cum_sum_matrix[i + 1][j + 1] = (
                h_cum_sum_matrix[i + 1][j] + matrix[i + 1][j + 1]
            )

    cum_sum_matrix = generate_matrix(h, w)
    # w方向の累積和を計算
    for i in range(h):
        for j in range(w):
            cum_sum_matrix[i + 1][j + 1] = (
                cum_sum_matrix[i][j + 1] + h_cum_sum_matrix[i + 1][j + 1]
            )

    return cum_sum_matrix


def generate_matrix(h: int, w: int) -> list[list[int]]:
    # 版兵を含めて生成する
    return [[0] * (w + 2) for _ in range(h + 2)]


if __name__ == "__main__":
    main()
