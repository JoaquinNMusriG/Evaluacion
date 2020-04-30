from claseProveedor import Proveedor
from claseComprobante import Comprobante
from ManejadorComprobantes import ManejadorComprobantes
from ManejadorProveedores import ManejadorProveedores

if __name__ == '__main__':

    comprobantes = ManejadorComprobantes()
    proveedores = ManejadorProveedores()

    comprobantes.cargarComprobantes()
    proveedores.cargarProveedores()

    cuit = input('Ingrese el cuit de un proveedor.')
    idprov = proveedores.buscarProveedorPorCUIT(cuit)

    print()
