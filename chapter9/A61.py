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
    N, M = LI()
    A, B = [], []
    for _ in range(M):
        a, b = LI()
        A.append(a)
        B.append(b)

    graph = {}
    for a, b in zip(A, B):
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]

    for k, v in graph.items():
        print("k:", k, "{", v, "}")


if __name__ == "__main__":
    main()
