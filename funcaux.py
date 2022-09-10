def copy_matrix(origen):
        destino=[]
        for i in range(len(origen)):
            destino.append(origen[i].copy())
        return destino