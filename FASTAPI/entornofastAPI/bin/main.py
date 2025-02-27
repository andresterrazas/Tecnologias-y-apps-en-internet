from fastapi import FastAPI, HTTPException
from typing import Optional, List
from modelsPydantic import modelUsuario

app= FastAPI(
    title='Mi primer API',
    description='Andres Terrazas',
    version= '1.0.2'
)

Usuarios=[
    {"id":1, "nombre":"Anettita", "edad":20, "correo":"anettita@example.com"},
    {"id":2, "nombre":"Isaac", "edad":22, "correo":"isaac@example.com"},
    {"id":3, "nombre":"Emilito", "edad":20, "correo":"emilito@example.com"},
    {"id":4, "nombre":"Brayan", "edad":20, "correo":"brayan@example.com"},
]

@app.get('/',tags=['Inicio'])
def main():
    return {'hola fastAPI':'Andrés Terrazas'}

#Endpoint consultar todos
@app.get('/usuarios',response_model= List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return Usuarios

#Endpoint para agregar usuarios
@app.post('/usuario/',response_model= modelUsuario,tags=['Operaciones CRUD'])
def AgregarUsuario(Usuario: modelUsuario):
    for usr in Usuarios:
        if usr["id"] == Usuario.id:
            raise HTTPException(status_code= 400, detail="El id ya está registrado, no seas baboso")

    Usuarios.append(Usuario)
    return Usuario

#endpoint para actualizar usuario
@app.put('/usuarios/{id}',response_model=modelUsuario, tags=['Operaciones CRUD'])
# lo que hace dict es que recibe un diccionario y lo pone como lista
def ActualizarUsuario(id: int, usuariosNuevos:modelUsuario):
    for index, usr in enumerate (Usuarios):
        if usr['id'] == id:
            Usuarios[index]= usuariosNuevos.model_dump()
            return Usuarios[index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
#endpoint para eliminar usuario
@app.delete('/usuarios/{id}',tags=["Operaciones CRUD"])
def EliminarUsuario(id:int):
    for i in range(len(Usuarios)):
        if Usuarios[i]["id"]==id:
            Usuarios.pop(i)
            return {"mensaje":"usuario eliminado"}
    raise HTTPException(status_code=404,detail="usuario no encontrado")