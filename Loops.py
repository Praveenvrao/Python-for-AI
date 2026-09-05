#While loop
i = 0
while i<=10:
    print(f"This is While loop line{i}")
    j = 1
    while j <=5:
        print(f"This is inner while loop{j}")
        j += 1

    i += 1

print(i)

#while loop

data = [12, 34, 56, 78, 90]

i = 0
n = len(data)
while i < n:
    print(data[i])
    i += 1

#for loop

Data1 = ["Mallik", 32, "John", True, 43.0]

for value in Data1:
    print(value)

for i in range(16):
    if i % 3 != 0:
       # continue
        break
    print(i)