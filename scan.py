import sys
from pathlib import Path


def read_lines(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def count_non_empty(lines):
    total = 0
    for line in lines:
        if line .strip():
            total += 1
    return total


def count_comments(lines):
    total = 0
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("//") or stripped.startswith("{"):
            total += 1
    return total


def main():
    path = Path(sys.argv[1])
    lines = read_lines(path)
    print(f"celkem{len(lines)}")
    print(f"neprazdne{count_non_empty(lines)}")
    print(f"komentare{count_comments(lines)}")


if __name__ == "__main__":
    main()
