from collections import deque

def invert(pref, N):
    d = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            d[i][pref[i][j]] = j
    return d

def define_stable_matching(pref_man, pref_women):
    N = len(pref_man)
    pref_women = invert(pref_women, N)
    husband = {}
    queue = deque(range(N))
    next_proposal = [0] * N

    while queue:
        m = queue.popleft()
        w = pref_man[m][next_proposal[m]]
        next_proposal[m] += 1

        if w not in husband:
            husband[w] = m
        else:
            m2 = husband[w]
            # check if woman prefers new man old man (m2)
            if pref_women[w][m] < pref_women[w][m2]:
                queue.append(m2)
                husband[w] = m
            else:
                queue.append(m)
    return husband

stable_match = define_stable_matching(
    pref_man = [
    [3, 1, 2, 0],
    [1, 0, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
],
pref_women = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
]
)
print(stable_match)
print([(stable_match[w], w) for w in range(len(stable_match))])



        

