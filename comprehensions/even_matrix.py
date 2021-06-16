i = int(input())
print([[x for x in map(int, input().split(", ")) if x % 2 == 0] for i in range(i)])
