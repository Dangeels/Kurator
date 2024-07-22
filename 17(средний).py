f = open('17(средний)')

arr = [int(i) for i in f]

arrows = 0
deaths = 0
count_days = 0
soldiers = 0

for i in range(len(arr)-2):
    v = sorted(arr[i:i+3])
    arrows+=max(v)
    deaths+=v[1]

average = deaths/arrows

for i in range(len(arr)-2):
    v = sorted(arr[i:i+3])
    if v[1]/v[2] > average:
        count_days+=1
        soldiers+=v[1]
print(count_days, soldiers)