n = int(input())
a = input().split()
x = input()
s = ' '
i = 0
while (i<n):
    if (x == a[i]):
        s = s + ' ' + str(i+1)
        i +=1
if (s == ' '):
    print(-1)
else:
    print(s.strip())
