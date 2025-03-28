from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
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

#Endpoint de inicio
@app.get('/',tags=['Inicio'])
def main():
    return {'hola fastAPI':'Andrés Terrazas'}
    
#dependencies=[Depends(BearerJWT())]    
    
#Endpoint consultar todos
@app.get('/usuarios/',tags=['Operaciones CRUD'])
def ConsultarTodos():
    db= Session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        raise HTTPException(status_code=500, content={"mensaje":"Error al consultar usuarios", "error":str(e)})
    finally:
        db.close()
        
#Endpoint consultar por id
@app.get('/usuarios/{id}',tags=['Operaciones CRUD'])
def ConsultarUno(id:int):
    db= Session()
    try:
        consulta= db.query(User).filter(User.id==id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje":"Usuario no encontrado"})
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        raise HTTPException(status_code=500, content={"mensaje":"Error al consultar el usuario", "error":str(e)})
    finally:
        db.close()

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

# Endpoint para actualizar usuario
@app.put('/usuarios/{id}', tags=['Operaciones CRUD'])
def ActualizarUsuario(id: int, usuariosNuevos: modelUsuario):
    db = Session()
    try:
        usuario_existente = db.query(User).filter(User.id == id).first()
        if not usuario_existente:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        # Actualizar los campos del usuario existente
        for key, value in usuariosNuevos.model_dump().items():
            setattr(usuario_existente, key, value)
        
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario actualizado", "usuario": usuariosNuevos.model_dump()})
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, content={"mensaje": "Error al actualizar usuario", "error": str(e)})
    finally:
        db.close()

# Endpoint para eliminar usuario
@app.delete('/usuarios/{id}', tags=["Operaciones CRUD"])
def EliminarUsuario(id: int):
    db = Session()
    try:
        usuario_existente = db.query(User).filter(User.id == id).first()
        if not usuario_existente:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        db.delete(usuario_existente)
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario eliminado"})
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, content={"mensaje": "Error al eliminar usuario", "error": str(e)})
    finally:
        db.close()
     
#endpoint para autenticación con JWT
@app.post('/auth',tags=['Autenticación'])
def login(autorizado:modelAuth):
    if autorizado.correo == 'andres@example.com' and autorizado.passw == '12345678':
        token:str = createToken(autorizado.model_dump())
        return JSONResponse(content=token)   
    else:
        return {"Aviso":"Usuario no autorizado"}