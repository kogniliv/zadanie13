import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import aseegg as ag

dane= pd.read_csv("C:/Users/Oliwia/Desktop/zadanie/proba113.csv", delimiter=',',engine = "python", names = ['number','sub01','sub02','sub03','sub04','last'])

#1 kolumna
signal = dane['sub01']
probkowanie = 200
time = len(signal)/200
t=np.linspace(0,time,time*200)

#filter
filter1 = ag.pasmowozaporowy(signal,probkowanie,49,51)
filter2 = ag.pasmowoprzepustowy(filter1,probkowanie,1,50)

#before
#plt.plot(t, signal, color="red")
#plt.xlabel("Czas[s]",size=10)
#plt.ylabel("Amplituda[-]",size=10)
#plt.show()

#after
#plt.plot(t,filter2, color ="brown")
#plt.xlabel("Czas[s]",size=10)
#plt.ylabel("Amplituda[-]",size=10)
#plt.show()

#last column
#last = dane['last']
#plt.plot(t,last,color="blue")
#plt.xlabel("Czas[s]",size=10)
#plt.ylabel("Amplituda[-]",size=10)
#plt.show()

#blink info
blink=[]
y=0
z=0
for x in filter2:
    if x>=0.05:
        if y<0.05:
            blink.append(dane['last'][z])
    z+=1

print("Kod otrzymany od osoby badanej to:", blink)
