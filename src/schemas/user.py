from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "password123",
            }
        }
