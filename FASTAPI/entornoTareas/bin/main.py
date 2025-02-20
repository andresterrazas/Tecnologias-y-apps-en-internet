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

# Obtener una tarea por ID
@app.get('/tareas/{tarea_id}', tags=['Tareas'])
def obtener_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail='Tarea no encontrada')

# Crear una nueva tarea
@app.post('/tareas', tags=['Tareas'])
def crear_tarea(tarea: dict):
    tareas.append(tarea)
    return tarea

# Actualizar una tarea existente
@app.put('/tareas/{tarea_id}', tags=['Tareas'])
def actualizar_tarea(tarea_id: int, titulo: Optional[str] = None, descripcion: Optional[str] = None, vencimiento: Optional[str] = None, estado: Optional[str] = None):
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            if titulo is not None:
                tarea['titulo'] = titulo
            if descripcion is not None:
                tarea['descripcion'] = descripcion
            if vencimiento is not None:
                tarea['vencimiento'] = vencimiento
            if estado is not None:
                tarea['estado'] = estado
            return tarea
    raise HTTPException(status_code=404, detail='Tarea no encontrada')