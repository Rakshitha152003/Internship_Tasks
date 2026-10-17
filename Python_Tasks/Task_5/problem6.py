# Problem 6: Introduction to Sets

# HackerRank Link:

# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
distinct_heights = set(array)
return sum(distinct_heights) / len(distinct_heights)


if **name** == '**main**':
n = int(input())
arr = list(map(int, input().split()))


result = average(arr)
print(result)

