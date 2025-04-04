import sys
print(sys.path)
from fastapi import FastAPI, HTTPException
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

from fastapi.middleware.cors import CORSMiddleware

app= FastAPI(
    title='Mi primer API',
    description='Andres Terrazas',
    version= '1.0.2'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(routerUsuario)
app.include_router(routerAuth)

#Endpoint de inicio
@app.get('/',tags=['Inicio'])
def main():
    return {'hola fastAPI':'Andrés Terrazas'}
