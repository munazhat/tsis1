#example1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#example2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#example3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#example4
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#example5
if a > b: print("a is greater than b")

#example6
a = 2
b = 330
print("A") if a > b else print("B")

#example7
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#example8
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#example9
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#example10
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#example11
a = 33
b = 200

if b > a:
  pass

#exercise1
a = 50
b = 10
if a > b:
  print("Hello World")