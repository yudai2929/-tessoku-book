import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


MAX_SCORE = 100


def main():
    N, K = LI()
    A, B = [], []
    for _ in range(N):
        a, b = LI()
        A.append(a)
        B.append(b)

    count_list = [0] * (MAX_SCORE + 1) ** 2
    for a in range(1, MAX_SCORE + 1):
        for b in range(1, MAX_SCORE + 1):
            count = calcCount(N, K, A, B, a, b)
            count_list.append(count)

    print(max(count_list))


def calcCount(
    N: int, K: int, A: list[int], B: list[int], min_a: int, min_b: int
) -> int:
    count = 0
    max_a = min_a + K
    max_b = min_b + K
    for i in range(N):
        if min_a <= A[i] <= max_a and min_b <= B[i] <= max_b:
            count += 1
    return count


if __name__ == "__main__":
    main()
