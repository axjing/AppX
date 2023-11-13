#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2023/10/25 21:16:47
@Author  :   axjing 
@Version :   0.1.0
@Desc    :   None
'''

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
                        

from .session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    # first_name = Column(String(255))
    # last_name = Column(String(255))
    username = Column(String(255), unique=True, index=True)
    password_hash = Column(String(1024))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)