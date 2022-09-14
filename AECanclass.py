
from ftplib import parse229
from valoresclass import clsvalores 
from configclass import clsconfig
from random import gauss, random,choice,randint,randrange,uniform,gauss
from funcaux import copy_matrix
from indclass import clsind
import sys
class clsAECan:
    def __init__(self,valores:clsvalores,config:clsconfig):
        self.valores=valores
        self.config=config
        self.i=[]#poblacion actual

        self.p=[]#padres
        self.h=[]#hijos
        self.m=[]#hijos mutados
        self.s=[]#supervivientes
        self.pesos=[]        
        self.min_fitness=0
        self.min_fitness_ant=0
        self.n_gen_terminacion=0
        self.soluc=[]
        self.n_generacion=0
    
    def initpob(self):
        #Lo voy a tratar como un problema de permutacion, donde hay que poner 9 9s, 9 8s,....9 1s. Teniendo en cuenta los 
        #valores que estan fijos en los valores dados
        self.i=[]
        self.h=[]
        self.m=[]
        self.s=[]

        while len(self.i)<self.config.poplen:                 
            ind=clsind()
            ind.x.append(uniform(self.valores.x1min,self.valores.x1max))
            ind.x.append(uniform(self.valores.x2min,self.valores.x2max))        
            ind.calc_fitness()
            self.i.append(ind)              
        self.__min_fitness()              

  
    def __min_fitness(self):
        self.min_fitness=0
        for i in range(len(self.i)):
            if self.min_fitness>self.i[i].fitness:
                self.min_fitness=self.i[i].fitness
                self.soluc=self.i[i].copy()
    
    def condicion_terminacion(self):           
        if self.n_gen_terminacion>self.config.n_gen_terminacion:
            return True
        else:
            return False

    
    def seleccion_padres(self):
        self.p=[]
        if self.config.tipo_seleccion_padres==0:
            for i in range(0,self.config.poplen):
                self.p.append(self.__torneo())
        elif self.config.tipo_seleccion_padres==1:
            P=[]
            sum_f=0
            for i in range(len(self.i)):
                sum_f+=(1/self.i[i].fitness)
            for i in range(len(self.i)):
                P.append((1/self.i[i].fitness/sum_f))#el 1- para minimizar
            L=[]
            L.append(0)
            for i in range(1,len(self.i)+1):
                L.append(L[i-1]+P[i-1])
            for i in range(0,self.config.poplen):
                self.p.append(self.__ruleta(L))

    def __torneo(self):
        pos_inds=[]  
        min_fitness=0  
        pos_ganador=0    
        while len(pos_inds)<self.config.tamtorneo:
            pos_ind=randint(0,self.config.poplen-1)
            if (pos_ind not in pos_inds):
                pos_inds.append(pos_ind)
        for i in range(len(pos_inds)):
            if (min_fitness>self.i[pos_inds[i]].fitness):
                pos_ganador=pos_inds[i]
                min_fitness=self.i[pos_inds[i]].fitness                    
        return self.i[pos_ganador].copy()
    
    def __ruleta(self,L):
        r=random()
        for i in range(len(L)-2,-1,-1):
            if r>L[i]:
                return self.i[i].copy()
       



    def recombinar(self):
        max=len(self.p)-1
        self.h=[]
        while len(self.p)>0:
            #cogemos dos padres de manera aleatoria para cruzarlos y los sacamos de la lista
            pos=randint(0,max)
            p1=self.p[pos]
            self.p.remove(p1)
            max-=1
            pos=randint(0,max)
            p2=self.p[pos]
            self.p.remove(p2)
            max-=1
            pc=random()           
            #calculamos un valor entre 0 y 1 y si es menor que pc cruzamos y si no los pasamos a los hijos
            if (pc>=self.config.pc):
                self.h.append(p1)
                self.h.append(p2)
            else:
                alpha=random()
                h1=clsind()
                h2=clsind()
                balanceo=True
                for i in range(len(p1.x)):
                    if balanceo:
                        h1.x.append(alpha*p1.x[i])
                        h2.x.append((1-alpha)*p2.x[i])
                    else:
                        h1.x.append(alpha*p2.x[i])
                        h2.x.append((1-alpha)*p1.x[i])
                    balanceo=not balanceo
                    self.h.append(h1)
                    self.h.append(h2)



   
    

    def mutacion(self):
        self.m=[]                
        i=0
        for i in range(len(self.h)):
            m=clsind()
            m=self.h[i].copy()
            pm=random()
            if pm<self.config.pm:
                alpha=gauss(0,self.config.sigma)
                for j in range(len(self.h[i].x)):
                    m.x[j]=self.h[i].x[j]+alpha
            if m.x[0]>self.valores.x1max:
                m.x[0]=self.valores.x1max
            elif m.x[0]<self.valores.x1min:
                m.x[0]=self.valores.x1min
            if m.x[1]>self.valores.x2max:
                m.x[1]=self.valores.x2max
            elif m.x[1]<self.valores.x2min:
                m.x[1]=self.valores.x2min
            m.calc_fitness()
            self.m.append(m)
            
   


    def seleccion_supervivientes(self):
        #ordenamos self.i y self.m (burbuja)
        self.s=[]
        for i in range(len(self.i)-1):
            for j in range(len(self.i)-1-i):
                if self.i[j].fitness>self.i[j+1].fitness:
                    aux=self.i[j].copy()
                    self.i[j]=self.i[j+1].copy()
                    self.i[j+1]=aux.copy()
                if self.m[j].fitness>self.m[j+1].fitness:
                    aux=self.m[j].copy()
                    self.m[j]=self.m[j+1].copy()
                    self.m[j+1]=aux.copy()
        for i in range(0,self.config.elitismo):  
            if self.i[i].fitness<self.m[0].fitness:
                self.s.append(self.i[i].copy())
        i=0
        while len(self.s)<self.config.poplen:
            self.s.append(self.m[i])
            i+=1
        self.i=self.s
        
        self.n_generacion+=1
        self.min_fitness=self.i[0].fitness
        if self.min_fitness==self.min_fitness_ant:
            self.n_gen_terminacion+=1
        else:
            self.n_gen_terminacion=0
        self.min_fitness_ant=self.min_fitness
        print(str(self.n_generacion)+"-->"+str(self.i[0].fitness))
    '''   
    def __heuristica_ini(self):
        pass
    '''
