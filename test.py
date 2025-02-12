from collections import deque

def josephus(ls, skip):
    d = deque(ls)
    survivor = None
    
    while d:
        d.rotate(-skip)
        survivor = d.popleft()
    
    return survivor

n = 7 
k = 3
people = list(range(1, n + 1))
print("El sobreviviente es:", josephus(people, k))
