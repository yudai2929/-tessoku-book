import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


MAX_DIGIT = 10


def main():
    N = I()

    binary = to_binary(N)

    binary_embed_zero = embed_zero(binary)

    str_binary = list_to_str(binary_embed_zero)

    print(str_binary)


def embed_zero(binary: list[int]) -> list[int]:
    while len(binary) < MAX_DIGIT:
        binary.insert(0, 0)
    return binary


def to_binary(mut_n: int) -> list[int]:
    binary = []
    while mut_n > 0:
        binary.append(mut_n % 2)
        mut_n //= 2
    return binary[::-1]


def list_to_str(list: list[int]) -> str:
    return "".join(map(str, list))


if __name__ == "__main__":
    main()
