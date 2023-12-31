#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   crud.py
@Time    :   2023/10/25 21:17:45
@Author  :   axjing 
@Version :   0.1.0
@Desc    :   CRUD:create, read, update, delete
'''

import typing as t

from core.security import get_password_hash, verify_password
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_users_by_user(db:Session,username:str)->schemas.UserBase:
    user = db.query(models.User).filter(models.User.username == username).first()
    # if not user:
    #     raise HTTPException(status_code=404, detail="User not found")
    return user

def get_users_by_email(db: Session, email: str) -> schemas.UserBase:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.UserOut]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        # first_name=user.first_name,
        # last_name=user.last_name,
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return user


def edit_user(
    db: Session, user_id: int, user: schemas.UserEdit
) -> schemas.User:
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    update_data = user.dict(exclude_unset=True)

    if "password" in update_data:
        update_data["password_hash"] = get_password_hash(user.password)
        del update_data["password"]

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
