a, b = map(int, input().split())
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

ten = 0
for i in range(n):
    ten += arr[i]*(a**i)

result = []
while ten // b:
    result.append(ten % b)
    ten = ten // b
result.append(ten)
result.reverse()
print(' '.join(map(str, result)))