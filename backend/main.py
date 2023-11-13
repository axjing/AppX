#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/10/30 22:38:11
@Author  :   axjing 
@Version :   0.1.0
@Desc    :   None
'''


from typing import List

import httpx
from core import config
from db import crud, models, schemas
from db.session import SessionLocal, engine
from fastapi import Depends, FastAPI, Form, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware  # 解决跨域
from sqlalchemy.orm import Session
from starlette.requests import Request

description="一个有理想的仓库"
app = FastAPI(
    title=config.PROJECT_NAME,
    description=description#, docs_url="/docs", openapi_url="/"
)

# 配置允许域名
origins = [
    # "http://127.0.0.1",
    # "http://127.0.0.1:3000",
    "http://localhost",
    "http://localhost:3000",
]
# 配置允许域名列表、允许方法、请求头、cookie等
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}
#依赖
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# app.post("/users/", response_model=schemas.User)
# 路由路径，注册用户
@app.post("/register", response_model=schemas.User)
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 根据用户命查找用户
    db_user=crud.get_users_by_user(db,username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    # 根据email查找用户
    db_user = crud.get_users_by_email(db, email=user.email)
    # 如果用户存在，提示该邮箱已经被注册
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # 返回创建的user对象
    user=crud.create_user(db=db, user=user)
    return user
    # return {"message": "User registered successfully"}

# 用户登录
# @app.post("/login", response_model=schemas.User)
@app.post("/login")
async def login_user(username: str = Form(...), password:str = Form(...),db: Session = Depends(get_db)):
    # 获取当前id的用户信息
    user = crud.get_users_by_user(db, username=username)
    # 如果没有信息，提示用户不存在
    if not user or not crud.verify_password(password, str(user.password_hash)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # return user
    return {"message": "Login successful"}
# @app.get("/users/read/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     # 读取指定数量用户
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
# @app.post("/chat")
# async def chat(prompt: str = Form(...)):
#     # 在OpenAI上获取您的API密钥
#     api_key = "YOUR_OPENAI_API_KEY"
#     api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"
#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             api_url,
#             headers={"Authorization": f"Bearer {api_key}"},
#             json={
#                 "prompt": prompt,
#                 "temperature": 0.7,
#                 "max_tokens": 150,
#             },
#         )
        
#         if response.status_code == 200:
#             data = response.json()
#             completion = data["choices"][0]["text"]
#             return {"response": completion}
#         else:
#             raise HTTPException(status_code=500, detail="GPT-3 API request failed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", reload=True, port=8000)
