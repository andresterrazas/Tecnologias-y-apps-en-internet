from pydantic import BaseModel,Field, EmailStr

#modelo para validación de datos
class modelUsuario(BaseModel):
    name:str = Field(..., min_length=3, max_length=15, description="Nombre debe contener solo letras y espacios")
    age:int 
    email:str 
    
class modelAuth(BaseModel):
    correo:EmailStr
    passw:str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña debe contener al menos 8 caracteres")