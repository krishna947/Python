for _ in range(int(input())):
    m,n = int(input()), int(input())
    arr = list(map(int, input().split()))

    s=[]
    for i in range(n):
        temp = m - arr[i]
        if temp in s:
            print(s.index(temp)+1, i+1)
        s.append(arr[i])