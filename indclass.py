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
        #calculamos el valor de la funcion de Mishra Bird
        #f(x1,x2))sin(x2)exp(1-cos(x1))^2+cos(x1)exp(1-sin(x2))^2+(x1-x2)^2
        valor=math.sin(self.x[1])*math.pow(math.exp(1-math.cos(self.x[0])),2)+math.cos(self.x[0])*math.pow(math.exp(1-math.sin(self.x[1])),2)+math.pow((self.x[0]-self.x[1]),2)
        
        self.fitness=valor
   