import csv
from claseComprobante import Comprobante

class ManejadorComprobantes:
    __comprobantes= []
    __cantidadProveedores=0
    __cantidadDias=30

    def __init__(self, cantidadProveedores=10): #revisar
        self.__comprobantes = []

    def agregarComprobante(self, idProveedor, dia, unComprobante): #revisar x2
        self.__comprobantes.append(unComprobante)

    def cargarComprobantes(self):
        archivo = open('comprobantes042020.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for comprob in reader:
            if (comprob[0].isdigit()) & (comprob[1].isdigit()) & (comprob[2] != '') & (comprob[3] != '') & (comprob[4].isdigit()) & (comprob[5].isdigit()) & (comprob[6].isdigit()) & (comprob[7].isdigit()) & (comprob[8] != ''):
                unComprobante = Comprobante(int(comprob[0]), int(comprob[1]), comprob[2], comprob[3], int(comprob[4]), int(comprob[5]), int(comprob[6]), int(comprob[7]), comprob[8])
                self.__comprobantes.agregarComprobante(int(comprob[0]), int(comprob[4]), unComprobante)
        archivo.close()

    def __str__(self):
        for i in range(len(self.__comprobantes)): #revisar x3
            cadena+=str(self.__comprobantes[i])
        return cadena

    def comprobantesPorProveedor(self, idProveedor):
	    for comprob in self.__comprobantes:
            if (comprob.getIdProveedor() == idProveedor):
                print (comprob())

    def buscarComprobantePorNumero(self, numeroComprobante):
        for comprob in self.__comprobantes:
            if (comprob.getNumeroComprobante() == numeroComprobante):
                if (comprob.getTipoComprobante() == 'F'):
                    comprob.setEstado('P')

    def facturasImpagasParaUnDia(self, dia, mP): #q es mp
        pass
