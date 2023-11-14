#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   schemas.py
@Time    :   2023/10/25 21:16:09
@Author  :   axjing 
@Version :   0.1.0
@Desc    :   None
'''

import typing as t

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username:str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False


class UserOut(UserBase):
    pass

class UserLogin(BaseModel):
    username:str
    password:str

class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserEdit(UserBase):
    password: t.Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    permissions: str = "user"
