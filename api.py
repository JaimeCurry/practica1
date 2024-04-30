from fastapi import FastAPI
from articulos import Articulo
from datetime import date

app = FastAPI()
listaArticulos = []

@app.post("/articulos/crearArticulo")
def crearArticulo(articulo: Articulo):
    listaArticulos.append(articulo)
    return articulo

@app.delete("/articulos/borrarArticulo/{id}")
def borrarArticulo(id: int):
    for articulo in listaArticulos:
        if(articulo.id == id):
            listaArticulos.remove(articulo)
            return articulo
    return {"message": "NO EXISTE NINGÚN ARTICULO QUE TENGA ESE ID"}

@app.put("/articulos/modificarArticulo/{id}")
def modificarArticulo(id: int,articuloModificado: Articulo):
    for articulo in listaArticulos:
        if(articulo.id == id):
            articulo.titulo = articuloModificado.titulo
            articulo.autor = articuloModificado.autor
            articulo.contenido = articuloModificado.contenido
            articulo.creado = articuloModificado.creado
            articulo.categoria = articuloModificado.categoria

            return articulo
    return {"message": "NO EXISTE NINGUN ARTICULO QUE TENGA ESE ID"}

@app.get("/articulos/buscarArticuloId/{id}")
def buscarArticuloId(id: int):
    for articulo in listaArticulos:
        if(articulo.id == id):
            return articulo
    return {"message": "NO EXISTE NNINGÚN ARTICULO CON ESTE ID"}

@app.get("/articulos/mostrarArticulos")
def mostrarArticulos():
    return listaArticulos


