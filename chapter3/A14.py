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
    B = LI()
    C = LI()
    D = LI()

    X = direct_product_add(A, B)
    Y = direct_product_add(C, D)
    Y.sort()

    for x in X:
        if binary_search(Y, K - x):
            print("Yes")
            return

    print("No")


def binary_search(nums: list[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def direct_product_add(a_list: list[int], b_list: list[int]) -> list[int]:
    result = []
    for a in a_list:
        for b in b_list:
            result.append(a + b)
    return result


if __name__ == "__main__":
    main()
