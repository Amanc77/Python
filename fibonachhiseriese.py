n = int(input("enter number of term  " ))
a = 0
b = 1
for i in range(1,n):
    print(a)
    c = a + b
    a = b
    b = c
print(i)