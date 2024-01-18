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

    if contains(A, K):
        print('Yes')
    else:
        print('No')

def contains(arr:list[int], target:int) -> bool:
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

if __name__ == '__main__':
    main()