def add(a, b, precission=8):

   a=float(a)
   b=float(b)
   return  round(a + b, precission)


print(add(1,2))
print(add(1.1,2.2))
print(add("1","2"))
print(add("1.1","2.2", 20))
print(add("1.1","2.2", None))
