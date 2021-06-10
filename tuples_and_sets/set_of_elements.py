n, m = map(int, input().split())

n_set = set()
m_set = set()

for _ in range(n):
    number = int(input())
    n_set.add(number)

for _ in range(m):
    number = int(input())
    m_set.add(number)

match = n_set & m_set

for el in match:
    print(el)
