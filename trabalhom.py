#| Operação                         | Complexidade                                                 |
#| -------------------------------- | ------------------------------------------------------------ |
#| `max(freq.items(), key=...)`     | O(k)                                                         |
#| `del freq[x]` / `freq[x-1]+=cnt` | O(1)                                                         |
#| Iterações totais                 | soma de todos `ai`                                           |
#| **Complexidade total**           | O((soma de todos `ai`) * k) → impraticável para grandes `ai` |

from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    alice = 0
    bob = 0
    turn = 0 

    freq = Counter(a)
    
    while freq:

        x, cnt = max(freq.items(), key=lambda item: item[1])

        points = cnt
        if turn == 0:
            alice += points
        else:
            bob += points

        del freq[x]
        if x-1 > 0:
            freq[x-1] += cnt
        
        turn ^= 1
    
    print(alice, bob)