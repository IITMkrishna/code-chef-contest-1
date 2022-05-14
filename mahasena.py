s = int(input())
w = input()
ws = w.split(" ")
a = len(ws)
i = 0
b = int(ws[i])
e = 0
o = 0

z = 1<=s<=100 and 1<=b<=100
if (z and s == a):
 while(i <= a-1):
   b = int(ws[i])
   if(b%2 == 0):
     e = e+1
   else:
     o = o+1
   i = i+1
 if(e>o):
   print('READY FOR BATTLE')
 else:
   print('NOT READY')
else:
  print('NOT READY')
