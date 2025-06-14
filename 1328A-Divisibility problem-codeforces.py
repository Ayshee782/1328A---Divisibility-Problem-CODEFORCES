A=int(input())

for _ in range (A):
    a, b = map (int,input().split())
    if a%b == 0:
        print(0)
    else:
        print(b-(a%b))