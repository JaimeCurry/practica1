from datetime import date
from pydantic import BaseModel

class Articulo(BaseModel):
    id: int
    titulo: str
    autor: str
    contenido: str
    creado: date
    categoria: str
