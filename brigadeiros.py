[N, K, T] = [int(x) for x in input().split(" ")]
pratos = [int(x) for x in input().split(" ")]
cadeiras = [int(x) for x in input().split(" ")]
amigos = []
for i in range(N):
    if cadeiras[i] == 1:
        amigos.append(i)


def dist(i1, i2):
    r =  max(i1, i2) - min(i1, i2)
    if r == 0:
        r = 1
    return r

best = {e:i for i, e in enumerate(pratos)}
order = [p for p in pratos]
order.sort(key=lambda x: x/dist(best[x], min(amigos, key=lambda y:dist(best[x], y))), reverse=True)
# print(sum(order[:K]))
# exit()
pulos = T
brigs = 0 

for o in order:
    if len(amigos) == 0:
        break

    best_amigo = amigos[0]
    best_dist = dist(best[o], amigos[0])
    a = 0
    for i, amg in enumerate(amigos):
        d = dist(amg, best[o])
        if d < best_dist and d < pulos:
            best_amigo = amg
            best_dist = d
            a = i
    if best_dist > pulos:
        continue
    
    if amigos[a] != best[o]:
        pulos -= best_dist 
    brigs += o
    amigos.pop(a)
print(brigs)
# exit()


# occ = set()
# def max_b(amg_idx, pulos):
#     fren = pratos[amg_idx+1:min(N, amg_idx+pulos+1)]
#     tras = pratos[max(0, amg_idx-pulos):amg_idx]
#     # print("fren tras")
#     # print(fren)
#     # print(tras)
#     bf= 0
#     bfi= 0
#     bt= 0
#     bti= 0
#     for i, b in enumerate(fren):
#         if b > bf:
#             if amg_idx+i+1 in occ:
#                 continue
#             bf = b
#             bfi=i 
#     for i, b in enumerate(tras):
#         if b > bt:
#             if amg_idx-(len(tras)-i) in occ:
#                 continue
#             bt = b
#             bti=i 
#     if max(bt, bf, pratos[amg_idx]) == pratos[amg_idx]:
#         return pratos[amg_idx], amg_idx

#     if bt > bf:
#         return bt, amg_idx-(len(tras)-bti)
#     else:
#         return bf, amg_idx+bfi+1


# while len(amigos ) > 0 :
#     # print(occ)
#     melhor = 0
#     melhor_idx = 0
#     melhor_distannce = 2*N
#     aidx = 0
#     for a in amigos:
#         c, cidx = max_b(a, pulos)
#         # print(c, cidx)
#         if c/dist(cidx, a) > melhor/melhor_distannce:
#             melhor_idx = cidx
#             melhor = c
#             aidx = a
#             melhor_distannce = dist(melhor_idx, a)
#             # print(f"novo melhor {melhor} idx {melhor_idx} amigo {aidx}")

#     brigs += melhor
#     if aidx != melhor_idx:
#         pulos -= melhor_distannce
#     # print(f"{aidx} pulou para {melhor_idx}")
#     # print(f"novo pulos={pulos}")
#     for i, a in enumerate(amigos):
#         if a == aidx:
#             amigos.pop(i)
#             break
#     occ.add(melhor_idx)
# print(brigs)