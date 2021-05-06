x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
n = int(input("n: "))

lst = []

for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k != n:
                lst.append([i,j,k])
print(lst)

#com list comprehension
print(list([i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n))