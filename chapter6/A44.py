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
    N, Q = LI()
    Query = []
    for _ in range(Q):
        Query.append(LI())

    A = [i for i in range(0, N + 1)]

    is_reversed = False

    for q in Query:
        if q[0] == 1:
            if not is_reversed:
                index = q[1]
                value = q[2]
                A[index] = value
            else:
                index = q[1]
                value = q[2]
                A[N + 1 - index] = value
        if q[0] == 2:
            is_reversed = not is_reversed
        if q[0] == 3:
            if not is_reversed:
                index = q[1]
                print(A[index])
            else:
                index = q[1]
                print(A[N + 1 - index])


if __name__ == "__main__":
    main()
