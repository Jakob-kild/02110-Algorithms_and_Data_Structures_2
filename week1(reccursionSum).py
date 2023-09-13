n = int(input())
values = list(map(int, input().split()))

start = 0
end = n - 1

alice_sum = 0
bob_sum = 0

alice_turn = True

while start <= end:
    if alice_turn:
        alice_sum += max(values[start], values[end])
    else:
        bob_sum += max(values[start], values[end])

    if values[start] > values[end]:
        start += 1
    else:
        end -= 1
    alice_turn = not alice_turn

print(alice_sum, bob_sum)
