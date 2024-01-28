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
    A, B = LI()
    max_num = max(A, B)
    min_num = min(A, B)
    ans = calc_gcd(max_num, min_num)

    print(ans)


def calc_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return calc_gcd(b, a % b)


if __name__ == "__main__":
    main()
