# s1 = 'mithila'
# s2 = 'bhojanalaya'
# s3 = ''
# i = 0
# j = 0
# while i<=(len(s1)) or j<=(len(s2)):
#     s3 = s3 + s1[i] + s2[j]
#     i = i+1
#     j = j+1
# print(s3)

def solve(s, t):
   i = j = 0
   result = ""
   while i < len(s) and j < len(t):
      result += s[i] + t[j]
      i+=1
      j+=1
   while i < len(s):
      result += s[i]
      i += 1
   while j < len(t):
      result += t[j]
      j += 1
   return result
s = "major"
t = "generalawefaef"
print(solve(s, t))


