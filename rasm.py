f = open('rasm.txt')
data = f.readlines()
for i in range(len(data)):
    data[i] = ' '.join(map(lambda x: str(int(not bool(int(x)))),data[i].split()))
for i in data:
    print(i)