N = int(input())
arv = {1:1}
rev = {x: [] for x in range(1, N+1)}
for i, v in enumerate(input().split(" ")):
    arv[i+2] = int(v)
    rev[int(v)].append(i+2)

def fill(start, v: list[int]):
    v.extend(rev[start])
    for c in rev[start]:
        fill(c, v)

line = False
if len(max(list(rev.values()), key=lambda x: max(1, len(x)))) == 1:
    line = True


for _ in range(int(input())):
    r = [int(x) for x in input().split(" ")]
    if r[0] == 1:
        if line:
            print(r[1]-r[2])
            continue
        
        end = r[1]
        for _ in range(r[2]):
            end = arv[end]
        print(end)
    else:
        if line:
            new = [x for x in range(r[1]+1, N+1)]
            rev[r[1]] = new
            for c in new:
                arv[c] = r[1]
                rev[c] = []
            line = False
            continue

        new = []
        fill(r[1], new)
        rev[r[1]] = new
        for c in new:
            arv[c] = r[1]
        line = False
        if len(max(list(rev.values()), key=lambda x: max(1, len(x)))) == 1:
            line = True

