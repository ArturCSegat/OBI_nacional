[N, L, R] = [int(x) for x in input().split(" ")]
funcs = []
for _ in range(N):
    r = input().split(" ")
    funcs.append((int(r[0]), int(r[1])))

def do_f(x, fun):
    return fun[0]*x + fun[1]

def inter(fun1, fun2):
    return (fun2[1] - fun1[1]) / (fun1[0] - fun2[0])

count = 0 
if L == R:
    for f in funcs:
        for f2 in funcs:
            if f2[0] == f[0]:
                continue
            if inter(f, f2) == R:
                count+=1
    print(count)
    exit()

c = 0
a = funcs[0][0]
for f in funcs:
    if f[0] == a:
        c += 1
if c == len(funcs) - 1:
    for i in range(N-1):
        x = inter(funcs[i], funcs[len(funcs) - 1])
        if x > R:
            continue
        if x < L:
            continue
        count+=1
    print(count)
    exit()

for i, f in enumerate(funcs):
    for j in range(N):
        if f[0] == funcs[j][0]:
            continue
        x = inter(f, funcs[j])
        if x > R:
            continue
        if x < L:
            continue
        count+=1
print(count//2)
