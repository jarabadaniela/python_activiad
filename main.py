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