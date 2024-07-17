f = open('17(простой)')

arr = [int(i) for i in f]

res = []

for i in range(len(arr)-1):
    x = arr[i]+arr[i+1]
    if (x)%2==0:
        res.append(x)
print(len(res), max(res))