from pydantic import BaseModel,Field

#modelo para validación de datos
class modelUsuario(BaseModel):
    id:int = Field(..., gt=0, description="ID único y solo números")
    nombre:str = Field(..., min_length=3, max_length=15, description="Nombre debe contener solo letras y espacios")
    edad:int = Field(..., gt=0, lt=130, description="Edad debe ser mayor a 0")
    correo:str = Field(..., min_length=5, max_length=50, description="Correo debe ser válido", pattern="^[\w\.-]+@[\w\.-]+\.\w+$", example="andres@gmail.com")
