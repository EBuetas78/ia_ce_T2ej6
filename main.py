#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.command.config import config
from AECanclass import clsAECan
from indclass import clsind
from valoresclass import clsvalores 
from configclass import clsconfig

import argparse

'''
en esta version optimizaremos la funcion de Rastrigin del ejercicio 7 del tema 3 para n2
f(x1,x2)=20+(x1^2-10*cos(2pix1))+(x2^2-10*cos(2pix2))
para el rango -5.12<=x1<=5.12 y -5.12<=x2<=5.12
f(0,0)=0

'''


def AECanonico(AECan:clsAECan,config:clsconfig):
    aux=0
    
    finalizado=False
    while not finalizado:
        AECan.initpob()
        fitness_ant=0
        n_gen_igual_fitness=0
        reiniciar=False
        while (not finalizado and not reiniciar):
            
            AECan.seleccion_padres()
            AECan.recombinar()
            AECan.mutacion()
            AECan.seleccion_supervivientes()
            aux+=1
            if aux>=100:
                print(str(AECan.i[0].fitness)+"---n_generacion:"+str(AECan.n_generacion))
                aux=0  
            if fitness_ant==AECan.i[0].fitness:
                n_gen_igual_fitness+=1
            fitness_ant=AECan.i[0].fitness
            if n_gen_igual_fitness>=config.n_gen_reinicio:
                reiniciar=True
            if AECan.condicion_terminacion():
                finalizado=True
    
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-p','--param',help='Fichero que contiene los parametros del problame',default='valores.json')
    parser.add_argument('-c','--config',help='Fichero que contiene los parametros de configuracion del AE',default='config.json')
    args=parser.parse_args()
    param=clsvalores()  
    param.leer_param(args.param) 
    config=clsconfig()
    config.leer_config(args.config)
    AECan=clsAECan(param,config)

    #prueba()
    #prueba_ciclos()
    #prueba_insercion()

    AECanonico(AECan,config)
    print_soluc(AECan)
    pass


def print_soluc(AECan:clsAECan):
    print ("--------------------")
    print("f(",AECan.i[0].x[0],",",AECan.i[0].x[1],")=",AECan.i[0].fitness)

        
if __name__ == '__main__':
    main()