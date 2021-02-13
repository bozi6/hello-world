with open('works.txt', 'r') as f:

    data1 = f.read(4)
    print(data1)

    data2 = f.read(20)
    print(data2)

    data3 = f.read(10)
    print(data3)