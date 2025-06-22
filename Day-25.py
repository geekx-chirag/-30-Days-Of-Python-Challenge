from pydantic import BaseModel, EmailStr, Field

class UserProfile(BaseModel):
    name: str = Field(..., example="MarvelStudious")
    email: EmailStr = Field(..., example="marvelstudious@example.com")
    age: int = Field(..., ge=18, le=100, example=25)

user = UserProfile(name="MarvelStudious", email="MarvelStudious@example.com", age=20)
print(user)