from pydantic import BaseModel,Field

#modelo para validación de datos
class modelEnvios(BaseModel):
    CP:str = Field(min_length=5, max_length=5, description="Código Postal debe ser de 5 dígitos", example="76040")
    Destino:str = Field(..., min_length=6, max_length=50, description="Dirección de destino", example = "Calle 1")
    Peso:int = Field(..., gt=0, lt=500, description="Peso en Kg")