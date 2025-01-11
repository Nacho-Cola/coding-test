import sys
input = sys.stdin.readline

N, M = map(int,input().split())
poke = {}
for i in range(N):
    pokemon = input().strip()
    poke[f'{i+1}'] = pokemon
    poke[pokemon] = i+1
for _ in range(M):
    q = input().strip()
    print(poke[q])
    