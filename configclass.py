import json 
class clsconfig():
    def __init__(self):
        self.poplen=0
        self.pc=0.0
        self.pm=0.0     
        self.sigma=0.0   
        self.tamtorneo=0
        self.elitismo=0        
        self.tipo_seleccion_padres=0      
        self.n_gen_reinicio=200
        self.n_gen_terminacion=500
    
    def leer_config(self,nombre_fichero):
        with open(nombre_fichero) as j:
            datos=json.load(j)
        self.poplen=datos["poplen"] if "poplen" in datos else 0
        self.pc=datos["pc"] if "pc" in datos else 1.0
        self.pm=datos["pm"] if "pm" in datos else 0.0       
        self.sigma=datos["sigma"] if "sigma" in datos else 0.0   
        self.tamtorneo=datos["tamtorneo"] if "tamtorneo" in datos else 2
        self.elitismo=datos["elitismo"] if "elitismo" in datos else 1        
        self.tipo_seleccion_padres=datos["tipo_seleccion_padres"] if "tipo_seleccion_padres" in datos else 0        
        self.n_gen_reinicio=datos["n_gen_reinicio"] if "n_gen_reinicio" in datos else 300
        self.n_gen_terminacion=datos["n_gen_terminacion"] if "n_gen_terminacion" in datos else 300
        return 0

