from fastapi.responses import JSONResponse
from modelsPydantic import modelAuth
from tokenGen import createToken
from fastapi import APIRouter

routerAuth = APIRouter()

#endpoint para autenticación con JWT
@routerAuth.post('/auth',tags=['Autenticación'])
def login(autorizado:modelAuth):
    if autorizado.correo == 'andres@example.com' and autorizado.passw == '12345678':
        token:str = createToken(autorizado.model_dump())
        return JSONResponse(content=token)   
    else:
        return {"Aviso":"Usuario no autorizado"}