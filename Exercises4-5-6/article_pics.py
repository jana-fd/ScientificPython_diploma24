import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,10,20)
y1 = np.tan(x)
y2 = np.tan(x + 0.2)
y3 = np.tan(x + 0.4)
y4 = np.tan(x + 0.6)
y5 = np.tan(x + 0.8)
y6 = np.tan(x + 1)

# now we decide the actual figure size in inches
fig = plt.figure(figsize=(12,6))

plt.suptitle('Different tan plots',fontweight='bold', fontsize='x-large')
plt.subplots_adjust(hspace=0.3, top=0.8)
# create subplots 231 means make a 2x3 grid and this is the first plot
plt.subplot(231)
#these are here to show that you can do the same here as for a single plot
plt.title('fig(1)',fontsize = 'large',fontstyle='italic')
plt.ylabel('tan(x)',fontstyle='oblique')
plt.xlabel('x',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y1,color='r')

plt.subplot(232)
plt.title('fig(2)',fontsize = 'large',fontstyle='italic')
plt.ylabel('tan(x + 0.2)',fontstyle='oblique')
plt.xlabel('x',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y2,color='g')

plt.subplot(233)
plt.title('fig(3)',fontsize = 'large',fontstyle='italic')
plt.ylabel('tan(x + 0.4)',fontstyle='oblique')
plt.xlabel('x',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y3,color='b')

plt.subplot(234)
plt.title('fig(4)',fontsize = 'large',fontstyle='italic')
plt.ylabel('tan(x + 0.6)',fontstyle='oblique')
plt.xlabel('x',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y4,color='y')

plt.subplot(235)
plt.title('fig(5)',fontsize = 'large',fontstyle='italic')
plt.ylabel('tan(x + 0.8)',fontstyle='oblique')
plt.xlabel('x',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y5,color='c')

plt.subplot(236)
plt.title('fig(6)',fontsize = 'large',fontstyle='italic')
plt.ylabel('tan(x + 1)',fontstyle='oblique')
plt.xlabel('x',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y6,color='m')

# removed extra white space
plt.tight_layout()
#plt.show()
plt.savefig("article.png")
