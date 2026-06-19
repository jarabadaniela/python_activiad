from fastapi import FastAPIHTTPException
from pydantic import BaseModel
mi_app= FastAPI ()

@mi_app.get ("/proyecto")

def mensaje ():
    return{"proyecto": "este es el proyecto de clientes a desarrollar.."}


@mi_app.get ("/clientes")
def clientes ():
    mi_lista= ["zuleima","yober","quiroga","sunsi","kamila","mady"]
    return {"clientes": mi_lista}




