#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   init_data.py
@Time    :   2023/10/25 21:18:58
@Author  :   axjing 
@Version :   0.1.0
@Desc    :   None
'''


from db.crud import create_user
from app.db import models
from app.db.schemas import UserCreate
from app.db.session import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="{{cookiecutter.superuser_email}}",
            password="{{cookiecutter.superuser_password}}",
            is_active=True,
            is_superuser=True,
        ),
    )


if __name__ == "__main__":
    print("Creating superuser {{cookiecutter.superuser_email}}")
    init()
    print("Superuser created")
