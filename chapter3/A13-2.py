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
    N, K = LI()
    A = LI()

    count = 0
    for i in range(N):
        count += contains_count(A, K, i + 1, N - 1, A[i])

    print(count)


def contains_count(nums: list[int], target: int, start: int, end: int, a: int) -> int:
    left = start
    right = end

    count = 0

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] - a <= target:
            count = mid - start + 1
            left = mid + 1
        else:
            right = mid - 1

    return count


if __name__ == "__main__":
    main()
