from fastapi import HTTPException,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()
# dependencies = [Depends(BearerJWT())]

@routerUsuario.get('/usuarios', tags=['OPERACIONES CRUD'])
def ConsultarTodos():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500, content={'mensaje':'No fue posible hacer la consulta', 'error':str(x)})
    
    finally:
        db.close()
        
@routerUsuario.get('/usuarios/{id}', tags=['OPERACIONES CRUD'])
def consultaUsuario_por_id(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={'mensaje':'Usuario no encontrado'})
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500, content={'mensaje':'No fue posible hacer la consulta', 'error':str(x)})
    
    finally:
        db.close()
   
#end point para eliminar un usuario tipo delete     
@routerUsuario.delete('/usuarios/{id}', tags=['OPERACIONES CRUD'])
def borrarUsuario(id: int): #se recibe el id del usuario a eliminar se pone que es de tipo int
    db = Session() #se crea la sesion de la base de datos
    try: #se intenta hacer la consulta
        consulta = db.query(User).filter(User.id == id).first() #se hace la consulta 
        if not consulta: #se valida si el usuario existe
            return JSONResponse(status_code=404, content={'mensaje':'Usuario no encontrado'}) #se retorna un mensaje de error
        db.delete(consulta) #se elimina el usuario
        db.commit() #se guarda la transaccion
        return JSONResponse(content={'mensaje':'Usuario eliminado'}) #se retorna un mensaje de exito
    
    except Exception as x: #en caso de error se retorna un mensaje de error
        db.rollback() #se deshace la transaccion
        return JSONResponse(status_code=500, content={'mensaje':'No fue posible hacer la consulta', 'error':str(x)}) #se retorna un mensaje de error
    
    finally:
        db.close() #se cierra la conexion con la base de datos
        
#end point para actualizar un usuario tipo put con su id
@routerUsuario.put('/usuarios/{id}', tags=['OPERACIONES CRUD'])
def actualizarUsuario(id: int, usuarioActualizado: modelUsuario): #se recibe el id del usuario a actualizar y el modelo de usuario actualizado
    db = Session() #se crea la sesion de la base de datos
    try: #se intenta hacer la consulta
        consulta = db.query(User).filter(User.id == id).first() #se hace la consulta
        if not consulta: #se valida si el usuario existe
            return JSONResponse(status_code=404, content={'mensaje':'Usuario no encontrado'}) #se retorna un mensaje de error
        for key, value in usuarioActualizado.model_dump().items(): #.items() regresa una lista de tuplas con clave y valor y .model_dump() regresa el modelo de usuario actualizado
            setattr(consulta, key, value) #setattr() asigna el valor a la clave en la consulta
        db.commit()
        return JSONResponse(content={'mensaje':'Usuario actualizado'})
    
    except Exception as x:
        db.rollback()
        return JSONResponse(status_code=500, content={'mensaje':'No fue posible hacer la consulta', 'error':str(x)})
    
    finally:
        db.close()
        
# end point para guardar un usuario tipo post
@routerUsuario.post('/usuarios/',response_model= modelUsuario ,tags=['OPERACIONES CRUD']) #se agrega el modelo de respuesta
def guardarUsuario(usuarionuevo: modelUsuario): #se agrega el modelo de entrada
    db = Session() #se crea la sesion
    try: #se intenta guardar el usuario
        db.add(User(**usuarionuevo.model_dump())) #se agrega el usuario a la base de datos
        db.commit() #se guarda el usuario
        return JSONResponse(status_code=201, content={'mensaje':'Usuario guardado', 'usuario':usuarionuevo.model_dump()}) #se retorna el usuario guardado
    except Exception as e: #en caso de error se retorna un mensaje de error
        db.rollback() #se deshace la transaccion
        return JSONResponse(status_code=500, content={'mensaje':'Error al guardar el usuario', 'error':str(e)})
    finally:
        db.close()