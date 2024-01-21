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

    count = count_pairs(A, K)
    print(count)


def count_pairs(nums: list[int], target: int) -> int:
    count = 0
    left = 0
    for right in range(len(nums)):
        while nums[right] - nums[left] > target:
            left += 1
        count += right - left

    return count


if __name__ == "__main__":
    main()
