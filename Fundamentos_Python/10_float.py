x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print (x == y)

y_str = format(y, ".2g")
print(y_str)
print(y_str == str(x))

tolerance = 0.0000001
print(abs(x - y)< tolerance)