N = int(input())
alts = [int(x) for x in input().split(" ")]

    
    
def all_equal(v):
    for i in range(N):
        if i == 0:
            continue
        if v[i] != v[i-1]:
            return False
    return True

target = max(alts)
done = False
etapas = 0
while not done:
    if all_equal(alts):
        print(etapas)
        exit()
    L = 0
    R = 0
    best_count = 0
    mm = min(alts)

    for i, a in enumerate(alts):
        if a != mm:
            continue
        count = 1
        for j in range(i+1, N):
            if alts[j] != alts[i]:
                break
            count += 1
        if count > best_count:
            L = i
            R = i+count-1
            best_count = count
    if best_count == 1:
        m = 0
        for i in range(N):
            if alts[i] < alts[m]:
                m = i
        L = m
        R = m

    # print(f"executed etapas {L}-{R}")
    for i in range(L, R+1):
        alts[i] += 1
    etapas += 1
    # print(f"alts= {alts}")    
