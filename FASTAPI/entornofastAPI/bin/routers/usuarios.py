from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter


routerUsuario = APIRouter()
    
    
#Endpoint consultar todos
@routerUsuario.get('/usuarios/',tags=['Operaciones CRUD'])
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
@routerUsuario.get('/usuarios/{id}',tags=['Operaciones CRUD'])
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
@routerUsuario.post('/usuario/',response_model= modelUsuario,tags=['Operaciones CRUD'])
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
@routerUsuario.put('/usuarios/{id}', tags=['Operaciones CRUD'])
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
@routerUsuario.delete('/usuarios/{id}', tags=["Operaciones CRUD"])
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
     
