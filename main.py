from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
mi_app= FastAPI ()

@mi_app.get ("/proyecto")

def mensaje ():
    return{"proyecto": "este es el proyecto de clientes a desarrollar.."}


@mi_app.get ("/clientes")
def clientes ():
    mi_lista= ["zuleima","yober","quiroga","sunsi","kamila","mady"]
    return {"clientes": mi_lista}

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str


class Factura(BaseModel):
    id: int
    cliente_id: int
    vrtotal: float


class Transaccion(BaseModel):
    id: int
    vr_unitario: float
    cantidad: int
    factura_id: int
    
    @app.get("/clientes")
    def listar_clientes():
     return clientes

@mi_app.get("/clientes/{id}")
def obtener_cliente(id: int):
    for cliente in clientes:
        if cliente.id == id:
            return cliente

    raise HTTPException(404, "Cliente no encontrado")

@mi_app.post("/clientes")
def crear_cliente(cliente: Cliente):
    clientes.append(cliente)

    return {
        "mensaje": "Cliente creado",
        "cliente": cliente
    }

@mi_app.put("/clientes/{id}")
def actualizar_cliente(id: int, datos: Cliente):

    for i, cliente in enumerate(clientes):
        if cliente.id == id:
            clientes[i] = datos

            return {
                "mensaje": "Cliente actualizado",
                "cliente": datos
            }

    raise HTTPException(404, "Cliente no encontrado")

@mi_app.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    for cliente in clientes:
        if cliente.id == id:
            clientes.remove(cliente)

            return {
                "mensaje": "Cliente eliminado"
            }

    raise HTTPException(404, "Cliente no encontrado")

@mi_app.get("/facturas")
def listar_facturas():
    return facturas

@mi_app.get("/facturas/{id}")
def obtener_factura(id: int):

    for factura in facturas:
        if factura.id == id:
            return factura

    raise HTTPException(404, "Factura no encontrada")

@mi_app.post("/facturas")
def crear_factura(factura: Factura):

    facturas.append(factura)

    return {
        "mensaje": "Factura creada",
        "factura": factura
    }

@mi_app.put("/facturas/{id}")
def actualizar_factura(id: int, datos: Factura):

    for i, factura in enumerate(facturas):
        if factura.id == id:
            facturas[i] = datos

            return {
                "mensaje": "Factura actualizada",
                "factura": datos
            }

    raise HTTPException(404, "Factura no encontrada")

@mi_app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for factura in facturas:
        if factura.id == id:
            facturas.remove(factura)

            return {
                "mensaje": "Factura eliminada"
            }

    raise HTTPException(404, "Factura no encontrada")

@mi_app.get("/transacciones")
def listar_transacciones():
    return transacciones

@mi_app.get("/transacciones/{id}")
def obtener_transaccion(id: int):

    for transaccion in transacciones:
        if transaccion.id == id:
            return transaccion

    raise HTTPException(404, "Transacción no encontrada")

@mi_app.get("/transacciones/{id}")
def obtener_transaccion(id: int):

    for transaccion in transacciones:
        if transaccion.id == id:
            return transaccion

    raise HTTPException(404, "Transacción no encontrada")