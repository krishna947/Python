n,arr = int(input()), list(map(int, input().split()))
m,brr = int(input()), list(map(int, input().split()))

l = [0]*(max(arr+brr) + 1)

for x in arr:
    l[x] += 1
for x in brr:
    l[x] -= 1

print(*sorted([x for x in range(len(l)) if l[x] != 0 ]))

