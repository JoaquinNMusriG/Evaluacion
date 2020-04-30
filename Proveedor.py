class Proveedor:
    __idProveedor=0
    __razonSocial=''
    __cuit=''
    def __init__(self, idProvedor=0, razonSocial='', cuit=''):
        self.__idProveedor = idProvedor
        self.__razonSocial = razonSocial
        self.__cuit = cuit
    def getIdProveedor(self):
        return self.__idProveedor
    def getRazonSocial(self):
        return self.__razonSocial
    def getCuit(self):
        return self.__cuit
    def __str__(self):
        return "CUIT: %s, Proveedor: %s\n" % (self.__cuit, self.__razonSocial)
