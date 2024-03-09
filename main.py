from fastapi import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Users(BaseModel):
    name: str
    password: str
    cpf: str

@app.post("/create_users/")
async def create_user(user: Users) -> Users:
    user_name = user.name
    password = user.password
    cpf = user.cpf

    return {
        "msg": "we got data succesfully",
        "name": user_name,
        "password" : password,
        "CPF" :  cpf       
        }

@app.get("/users/")
async def get_users(users: Users) :
    return users

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)