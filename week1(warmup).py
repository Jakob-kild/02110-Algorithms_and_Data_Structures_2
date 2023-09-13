n = input()
array = list(map(int, input().split()))
count = 1

for i in range(1, len(array)):
    if array[i] > array[i-1]:
        count += 1
print(count)