print("Enter Number of Test Case -")
t = input()
print("Enter pattern string and text string -")
ans = []
for i in range(t):
    patstring = raw_input()
    bigstring = raw_input()
    if (patstring in bigstring) or (patstring[::-1] in bigstring):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print i
