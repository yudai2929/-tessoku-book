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
    N = I()
    print(calc_square_area(N))

def calc_square_area(a):
    return a * a

if __name__ == '__main__':
    main()