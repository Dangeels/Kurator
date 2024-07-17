f = open('17(средний)')

frame_time = int(f.readline())
hp = int(f.readline())

arr = [int(i) for i in f]

count = 0
for i in range(len(arr)-3):
    v = arr[i]+arr[i+1]
    if v<frame_time:
        count+=1
        if v+arr[i+2]<frame_time:
            hp-=arr[i+3]
print(count, hp)