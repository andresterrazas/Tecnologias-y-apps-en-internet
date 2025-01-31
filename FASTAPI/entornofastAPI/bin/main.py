from fastapi import FastAPI
from typing import Optional

app= FastAPI(
    title='Mi primer API',
    description='Andres Terrazas',
    version= '1.0.1'
)

Usuarios=[
    {"id":1, "nombre":"Anettita", "edad":20},
    {"id":2, "nombre":"Isaac", "edad":22},
    {"id":3, "nombre":"Emilito", "edad":20},
    {"id":4, "nombre":"Brayan", "edad":20},
]

@app.get('/',tags=['Inicio'])
def main():
    return {'hola fastAPI':'Andrés Terrazas'}

@app.get('/promedio',tags=['Mi calificacion'])
def promedio():
    return 10
#Parámetro Obligatorio
@app.get('/usuario/{id}', tags=['Parámetro obligatorio'])
def consultaUsuario(id:int):
    #Conexión a la BD FICTICIA
    #Consulta y responde 
    return {"Se encontró el usuario:": id}
#Parámetro Opcional
@app.get('/usuarioX', tags=['Parámetro opcional'])
def consultaUsuario2(id:Optional[int]= None):
    if id is not None:
        for usuario in Usuarios:
            if usuario ["id"] == id:
                return {"Mensaje":"Usuario encontrado","usuario":usuario}
        return{"Mensaje":f"Usuario no encontrado: {id}"}
    else:
        return{"Mensaje":"No proporcionó un ID"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consultaUsuario3(
    id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in Usuarios:
        if (
            (id is None or usuario["id"] == id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios encontrados": resultados}
    else:
        return {"Mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}