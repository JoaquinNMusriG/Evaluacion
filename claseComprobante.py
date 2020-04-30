class Comprobante:
    __idProveedor=0
    __idComprobante=0
    __numeroComprobante=''
    __tipoComprobante=''
    __dia=0
    __mes=4
    __anio=2020
    __importe=0.0
    __estado=''

    def __init__(self, idProveedor, idComprobante, numeroComprobante,tipoComprobante, dia, mes, anio, importe, estado='I'):
       self.__idProveedor = idProveedor
       self.__idComprobante = idComprobante
       self.__numeroComprobante = numeroComprobante
       self.__tipoComprobante = tipoComprobante
       self.__dia = dia
       self.__mes = mes
       self.__anio = anio
       self.__importe = importe
       self.__estado = estado

    def setEstado(self, nuevoEstado):
        if (nuevoEstado == 'I') or (nuevoEstado == 'P'):
            self.__estado = nuevoEstado
        else:
            print('Error al ingresar estado, se admite "P" o "I".')

    def getImporte(self):
        return self.__importe

    def getIdProveedor(self):
        return self.__idProveedor

    def getNumeroComprobante(self):
        return self.__numeroComprobante

    def getTipoComprobante(self):
        return self.__tipoComprobante

    def __str__(self):
        cadena ='%02d/%02d/%4d  %8s   %18s       %10.2f  %1s\n'%(self.__dia, self.__mes, self.__anio, self.__tipoComprobante,self.__numeroComprobante, self.__importe, self.__estado)
        return cadena
