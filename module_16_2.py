
from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def in_put():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_admin(admin: str = 'Fedor'):
    return {"message": f"Имя: {admin},"
                       f" Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def get_user(
    user_id:Annotated[
    int,Path(
        ge=1,
        le=100,
        description='Введите свой ID'
                    '(положительное целое число от 1 до 100)'
      )
    ]
):
    return {"message": f'Hello, {user_id}'}

@app.put('/user/{username}/{age}')
async def put_user(
    username:Annotated
    [str,Path(
        min_length=5,
        max_length=20,
        description='Имя пользователя'
                    '(от 5 до 20 символов)'
      )
    ],
    age:Annotated[
    int,Path(
        ge=18,
        le=120,
        description='Укажите возраст'
                    '(положительное целое число от 18 до 120)'
      )
    ]
) -> dict:
    return {
        "message":(
        f"Информация о пользователе."
        f" Имя: {username}, Возраст: {age}"
      )
    }



#   uvicorn module_16_2:app --reload

#   http://127.0.0.1:8000
#   http://127.0.0.1:8000/docs
#   http://127.0.0.1:8000/redoc