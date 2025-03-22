from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app= FastAPI(
    title='Mi primer API',
    description='Andres Terrazas',
    version= '1.0.2'
)

#Levanta las tablas definidas en modelos
Base.metadata.create_all(bind=engine)

Usuarios=[
    {"id":1, "nombre":"Anettita", "edad":20, "correo":"anettita@example.com"},
    {"id":2, "nombre":"Isaac", "edad":22, "correo":"isaac@example.com"},
    {"id":3, "nombre":"Emilito", "edad":20, "correo":"emilito@example.com"},
    {"id":4, "nombre":"Brayan", "edad":20, "correo":"brayan@example.com"},
]

@app.get('/',tags=['Inicio'])
def main():
    return {'hola fastAPI':'Andrés Terrazas'}

#endpoint para autenticación con JWT
@app.post('/auth',tags=['Autenticación'])
def login(autorizado:modelAuth):
    if autorizado.correo == 'andres@example.com' and autorizado.passw == '12345678':
        token:str = createToken(autorizado.model_dump())
        return JSONResponse(content=token)   
    else:
        return {"Aviso":"Usuario no autorizado"}
    
#Endpoint consultar todos
@app.get('/usuarios', dependencies=[Depends(BearerJWT())] ,response_model= List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return Usuarios

#Endpoint para agregar usuarios
@app.post('/usuario/',response_model= modelUsuario,tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo: modelUsuario):
    db= Session()
    try:
        db.add(User(**usuarionuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"mensaje":"Usuario agregado", "usuario": usuarionuevo.model_dump()})
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, content={"mensaje":"Error al agregar usuario", "error":str(e)})
        
    finally:
        db.close()

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