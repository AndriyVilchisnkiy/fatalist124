x = 25
y = 30
print(x, y)
x,y = y, x
def swap(x,y):
    x, y = y, x
    return x, y


print(x, y)
c = 3
print(c)
#tell me the difference
swap(x,y)
print(x,y)