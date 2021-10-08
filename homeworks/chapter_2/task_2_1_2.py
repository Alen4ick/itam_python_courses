n = int(input())
s = [int(i) for i in input().split()]
def summation(m):
    m = [m[i] if m[i] > 0 else abs(m[i])*2 for i in range(len(m))]
    maxim = max(m)
    return sum([x/maxim for x in m])
print(summation(s))
