# cook your dish here
for i in range(int(input())):
    n, k = map(int, input().split())
    final = []
    count = 1
    a = list(map(int, input().split()))
    z = len(a)
    for b in range(0, z):
       if k % a[b] == 0:
          final.append(a[b])
    if not final:
       print(-1)
    else:
       print(max(final))
       
