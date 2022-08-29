import matplotlib.pyplot as plt
import random


vonalszin = ['blue', 'red', 'yellow', 'green', 'black', 'gray', 'autumn', 'bone', 'cool', 'copper', 'flag',
             'hot', 'hsv', 'jet', 'pink', 'prism', 'spring', 'summer', 'winter']
plt.title('If x odd then (num * 3+1), if even then (num/ 2)')
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
    plt.plot(rajz, label='numbers', color=random.shuffle(vonalszin))
    rajz.clear()
plt.xlabel('Steps')
plt.ylabel('Numbers')
plt.show()
