import matplotlib.pyplot as plt
import random
# szam = int(input("szám"))
import pylab as pl

vonalszin = ['blue', 'red', 'yellow', 'green', 'black', 'gray', 'autumn', 'bone', 'cool', 'copper', 'flag',
             'hot', 'hsv', 'jet', 'pink', 'prism', 'spring', 'summer', 'winter']
plt.title('Ha x páratlan akkor * 3+1 ha páros akkor / 2')
rajz = []
for i in range(10):
    szam = random.randint(1, 20)
    rajz.append(szam)
    print(i, szam)
    while szam > 1:
        if (szam % 2) == 1:
            szam = szam * 3 + 1
        else:
            szam = szam // 2
        rajz.append(szam)
    plt.plot(rajz, label='számok', color=random.shuffle(vonalszin))
    rajz.clear()
plt.xlabel('Lépések')
plt.ylabel('Számok')
plt.show()
