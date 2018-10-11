import math
nUnknown = False

print("Input '?' for Sample size if sample size is unknown")
n = input("Sample size")
if n == "?":
  nUnknown = True
  m = input("Margin of error")
  m = float(m)
else:
  n = int(n)
  x = input("Sample mean")
  x = float(x)

s = input("Population standard deviation")
c = input("Confidence level")
s = float(s)
c = int(c)

if c == 80:
  z = 1.28
elif c == 90:
  z = 1.645
elif c == 95:
  z = 1.96
elif c == 99:
  z = 2.58

if nUnknown == False:
  i1 = x - z * (s/math.sqrt(n))
  i2 = x + z * (s/math.sqrt(n))
  i1 = "%.2f" % i1
  i2 = "%.2f" % i2
  print(str(i1) + ", " + str(i2))
else:
  suggestedn = ((z * s)/m) * ((z * s)/m)
  suggestedn = math.ceil(suggestedn)
  print("n =", suggestedn)
