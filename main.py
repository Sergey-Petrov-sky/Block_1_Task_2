string = input()
n = 0
m = 0
for i in string:
    n = n+1
    if n == 3:
        continue
    if i == 'c':
       m = m + 1
    if n == len(string):
        break
    print(i)
if m>0:
    print("found simbol 'c'")
else:
    print("simbol 'c' not foud")
print("string leangh ->", len(string))


