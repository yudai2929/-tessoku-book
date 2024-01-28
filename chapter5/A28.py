from enum import Enum
import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


DIVIDED_NUMBER = 10**4


class Operation(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"


def main():
    N = I()
    T, A = [], []
    for _ in range(N):
        t, a = LS()
        T.append(t)
        A.append(int(a))

    nums = []
    current_num = 0
    for i in range(N):
        if T[i] == Operation.ADD.value:
            current_num += A[i]
        elif T[i] == Operation.SUB.value:
            current_num -= A[i]
        elif T[i] == Operation.MUL.value:
            current_num *= A[i]

        if current_num >= DIVIDED_NUMBER:
            current_num %= DIVIDED_NUMBER

        if current_num < 0:
            current_num += DIVIDED_NUMBER

        nums.append(current_num)

    for i in range(N):
        print(nums[i])


if __name__ == "__main__":
    main()
