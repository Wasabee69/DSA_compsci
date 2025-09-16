from collections import deque as deque
#N = int(input())


N = 4
pref_man = [
    [3, 1, 2, 0],
    [1, 0, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
]
pref_women = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
]
def inverse(pref):
    d = {i:{} for i in range(N)}
    for i in range(N):
        for j in range(N):
            d[i][pref[i][j]] = j
    return d

pref_man = inverse(pref_man)
pref_women = inverse(pref_women)
husband = {}
queue = deque(list(range(N)))
next_proposal = [0] * N

while queue:
    m = queue.popleft()
    w = pref_man[m][next_proposal[m]]
    next_proposal[m] += 1

    if w not in husband:
        # velger første partner
        husband[w] = m
    else:
        m2 = husband[w]
        if pref_women[w][m2] < pref_women[w][m]:
            #bytter partner
            queue.append(m2)
            husband[w] = m
        else:
            queue.append(m)

print(husband)
print([(husband[w], w) for w in range(N)])



        
