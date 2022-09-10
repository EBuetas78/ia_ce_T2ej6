import json 
class clsvalores():
    def __init__(self):
        self.x1max=0
        self.x1min=-10
        self.x2max=0
        self.x2min=-6.5

    
    def leer_param(self,nombre_fichero):
        with open(nombre_fichero) as j:
            datos=json.load(j)
        self.x1max=datos["x1max"] 
        self.x1min=datos["x1min"] 
        self.x2max=datos["x2max"] 
        self.x2min=datos["x2min"] 

        return 0

