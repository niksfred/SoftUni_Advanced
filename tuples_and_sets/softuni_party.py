vips = set()
regular = set()

n = int(input())

for _ in range(n):
    code = input()
    if code[0].isdigit():
        vips.add(code)
    else:
        regular.add(code)

came = input()

while not came == "END":
    if came in vips:
        vips.remove(came)
    elif came in regular:
        regular.remove(came)
    
    came = input()

print(len(vips) + len(regular))
sorted_vips = sorted(vips)
for i in sorted_vips:
    print(i)
sorted_regulars = sorted(regular)
for i in sorted_regulars:
    print(i)
    