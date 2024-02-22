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
    Q = I()
    Query = []
    for _ in range(Q):
        Query.append(LS())

    hash_table = {}

    for q in Query:
        if q[0] == "1":
            key = q[1]
            value = q[2]
            hash_table[key] = value
        if q[0] == "2":
            key = q[1]
            print(hash_table[key])


if __name__ == "__main__":
    main()
