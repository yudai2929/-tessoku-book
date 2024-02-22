import sys

import heapq


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
        Query.append(LI())

    queue = []

    for q in Query:
        if q[0] == 1:
            heapq.heappush(queue, q[1])
        if q[0] == 2:
            print(queue[0])
        if q[0] == 3:
            heapq.heappop(queue)


if __name__ == "__main__":
    main()
