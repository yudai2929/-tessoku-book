import sys

from collections import deque


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def main():
    Q = I()
    Query = []
    for _ in range(Q):
        Query.append(LS())

    stack = deque()

    for q in Query:
        if q[0] == "1":
            stack.append(q[1])
        if q[0] == "2":
            print(stack[-1])
        if q[0] == "3":
            stack.pop()


if __name__ == "__main__":
    main()
