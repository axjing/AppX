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
import uvicorn
from core import config
from db import crud, models, schemas
from db.session import SessionLocal, engine
from fastapi import Depends, FastAPI, Form, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request

app = FastAPI(
    # title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
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
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 根据email查找用户
    db_user = crud.get_user_by_email(db, email=user.email)
    # 如果用户存在，提示该邮箱已经被注册
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # 返回创建的user对象
    return crud.create_user(db=db, user=user)


@app.get("/users/read/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # 读取指定数量用户
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# 用户登录
@app.post("/login", response_model=schemas.User)
def login(user_id: int, db: Session = Depends(get_db)):
    # 获取当前id的用户信息
    db_user = crud.get_user(db, user_id=user_id)
    # 如果没有信息，提示用户不存在
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/chat")
async def chat(prompt: str = Form(...)):
    # 在OpenAI上获取您的API密钥
    api_key = "YOUR_OPENAI_API_KEY"
    api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            api_url,
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "prompt": prompt,
                "temperature": 0.7,
                "max_tokens": 150,
            },
        )
        
        if response.status_code == 200:
            data = response.json()
            completion = data["choices"][0]["text"]
            return {"response": completion}
        else:
            raise HTTPException(status_code=500, detail="GPT-3 API request failed")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)