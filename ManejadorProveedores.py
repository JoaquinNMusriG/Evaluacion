import csv
from claseProveedor import Proveedor

class ManejadorProveedores:
    __proveedores=[]
    def __init__(self):
	self.__proveedores = []
    def agregarProveedor(self, unProveedor):
        self.__proveedores.append(unProveedor)
    def cargarProveedores(self):
        archivo = open('proveedores.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for prov in reader:
            if (prov[0].isdigit()) & (prov[1] != '') & (prov[2] != ''):
                unProveedor = Proveedor(int(prov[0]), prov[1], prov[2])
                self.__proveedores.agregarProveedor(unProveedor)
        archivo.close()
    def __str__(self):
        cadena ='Proveedores:\n'
        cadena +='------------\n'
        for i in range(len(self.__proveedores)):
            cadena+=str(self.__proveedores[i])
        return cadena
    def buscarProveedorPorIdProveedor(self, idProveedor):
        for prov in self.__proveedores:
                if (prov.getIdProveedor() == idProveedor):
                    return prov.getRazonSocial()       #????

    def buscarProveedorPorCUIT(self, cuit):
        for prov in self.__proveedores:
            if (prov.getCuit() == cuit):
                return prov.getIdProveedor()
