import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def Str():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()
    S = Str()

    ans = False

    for i in range(N - 2):
        if S[i] == "R" and S[i + 1] == "R" and S[i + 2] == "R":
            ans = True
            break
        if S[i] == "B" and S[i + 1] == "B" and S[i + 2] == "B":
            ans = True
            break

    print("Yes" if ans else "No")


if __name__ == "__main__":
    main()
