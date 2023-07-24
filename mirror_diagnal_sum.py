def diagonalSum(arr, n):
    val = 0
    for i in range(n):
        sum = 0
        for j in range(n-1, -1, -1):
            if i < n and j >= 0:
                sum += arr[i][j]
        val = sum
    return val

n = int(input())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

val = diagonalSum(arr, n)
print(val)
