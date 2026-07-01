from pydantic import BaseModel


class OCRRequest(BaseModel):
    imagen: str