# Problem 8: Set .add()

# HackerRank Link:

# https://www.hackerrank.com/challenges/py-set-add/problem

if **name** == '**main**':
n = int(input())
countries = set()


for _ in range(n):
    country = input().strip()
    countries.add(country)

print(len(countries))

