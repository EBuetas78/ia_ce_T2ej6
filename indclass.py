from funcaux import copy_matrix
import math

class clsind:
    def __init__(self):
        self.x=[] #i[0]=x1;i[1]=x2
        self.fitness=0
        
    def copy(self):
        respuesta=clsind()
        respuesta.x=self.x.copy()
        respuesta.fitness=self.fitness        
        return respuesta

    def calc_fitness(self):
        #calculamos el valor de la funcion de Rastrigin        
        valor=20+(math.pow(self.x[0],2)-10*math.cos((2*math.pi*self.x[0])))+(math.pow(self.x[1],2)-10*math.cos((2*math.pi*self.x[1])))
        self.fitness=valor
   