from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title='API de Gestión de Tareas',
    description='API para gestionar una lista de tareas (To-Do List)',
    version='1.0.0'
)

# Lista de tareas simulando una base de datos
tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de TAI", "vencimiento": "2024-02-14", "estado": "completada"}
]

#Home
@app.get('/', tags=['Home'])
def inicio():
    return {'Bienvenido a la API de Gestión de Tareas'}

# Obtener todas las tareas
@app.get('/tareas', tags=['Tareas'])
def obtener_tareas():
    return tareas

