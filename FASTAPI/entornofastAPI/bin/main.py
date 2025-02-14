from fastapi import FastAPI, HTTPException
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

#Endpoint consultar todos
@app.get('/usuarios',tags=['Operaciones CRUD'])
def ConsultarTodos():
    return{"Usuarios registrados ": Usuarios}

#Endpoint para agregar usuarios
@app.post('/usuario/',tags=['Operaciones CRUD'])
def AgregarUsuario(Usuario: dict):
    for usr in Usuarios:
        if usr["id"] == Usuario.get("id"):
            raise HTTPException(status_code= 400, detail="El id ya está registrado, no seas baboso")

    Usuarios.append(Usuario)
    return Usuario

#endpoint para actualizar usuario
@app.put('/usuarios/{id}', tags=['Operaciones CRUD'])
# lo que hace dict es que recibe un diccionario y lo pone como lista
def ActualizarUsuario(id: int, usuariosNuevos: dict):
    for index, usr in enumerate (usuarios):
        if usr['id'] == id:
            usuarios[index].update(usuariosNuevos)
            return usuarios[index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
#endpoint para eliminar usuario
@app.delete('/usuarios/{id}',tags=["Operaciones CRUD"])
def EliminarUsuario(id:int):
    for i in range(len(Usuarios)):
        if Usuarios[i]["id"]==id:
            Usuarios.pop(i)
            return {"mensaje":"usuario eliminado"}
    raise HTTPException(status_code=404,detail="usuario no encontrado")