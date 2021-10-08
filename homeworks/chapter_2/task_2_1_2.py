n = int(input())
s = [int(i) for i in input().split()]
def summation(m):
    m = [i if i > 0 else abs(i)*2 for i in m]
    maxim = max(m)
    return sum([x/maxim for x in m])
