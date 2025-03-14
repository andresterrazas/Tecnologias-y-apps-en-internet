from fastapi import FastAPI, HTTPException
from modelspydantic import modelEnvios
from typing import Optional, List

app = FastAPI(
    title='Api de envíos',
    description='Exámen 2do parcial: Andres Terrazas Hernández',
    version='1.0.0'
)

Envios = [
    {"CP": "76040", "Destino": "Calle 1", "Peso": 10},
    {"CP": "76148", "Destino": "Calle 2", "Peso": 20},
    {"CP": "76052", "Destino": "Calle 3", "Peso": 30},
    {"CP": "76150", "Destino": "Calle 4", "Peso": 40}
]

# Endpoint consultar todos
@app.get('/Envios/{Envios_CP}', response_model=modelEnvios, tags=['Operaciones CRUD'])
def obtener_envio(Envios_CP: str):
    for Envio in Envios:
        if Envio['CP'] == Envios_CP:
            return Envio
    raise HTTPException(status_code=404, detail='Envio no encontrado')

@app.put('/Envios/{Envios_CP}', response_model=modelEnvios, tags=['Operaciones CRUD'])
def actualizar_envio(Envios_CP: str, envio: modelEnvios):
    for Envio in Envios:
        if Envio['CP'] == Envios_CP:
            Envio.update(envio)
            return Envio
    raise HTTPException(status_code=404, detail='Envio no encontrado')