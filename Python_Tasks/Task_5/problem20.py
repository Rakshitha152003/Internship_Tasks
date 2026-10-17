# Problem 20: Piling Up!

# HackerRank Link:

# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

if __name__ == '__main__':
T = int(input())


for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))

    last_block = float('inf')
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()

        if current > last_block:
            possible = False
            break

        last_block = current

    print("Yes" if possible else "No")

