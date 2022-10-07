import pickle

class Vehiculo:
    modelo=''
    color=''

    def __init__(self,modelo,color):
        self.modelo=modelo
        self.color=color

    def getModelo(self):
        return self.modelo
    def __str__(self):
        return f'Este es un vehiculo de tipo {self.modelo} y color {self.color}'

coche=Vehiculo('deportivo','rojo')

f=open('dato.bin','wb')
pickle.dump(coche,f)
f.close()

g=open('dato.bin','rb')
ferrari=pickle.load(g)
f.close()

print(type(ferrari))
print(ferrari.getModelo())

