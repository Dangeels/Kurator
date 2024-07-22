f = open('17(сложный)')

frame_time = int(f.readline())
hp = int(f.readline())

arr = [int(i) for i in f]

count_attacks = 0
defeated = False

for i in range(len(arr)-3):
    abs_dct = {abs(j): j for j in arr[i:i+4]}
    v = sorted(list(abs_dct.keys()))
    dmg = abs_dct[max(v)]
    effect = abs_dct[min(v)] if min(v)!=0 else abs_dct[v[1]]
    dodge = abs_dct[v[2]]
    attack_time = abs_dct[v[1]] if min(v)!=0 else abs_dct[v[0]]
    if attack_time!=0 and frame_time-(attack_time+dodge)>=0:
        hp-=dmg
        if dmg>0:
            count_attacks+=1
    if hp<=0:
        defeated=True
print(count_attacks, hp, defeated)