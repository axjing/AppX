#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   session.py
@Time    :   2023/10/25 21:14:37
@Author  :   axjing 
@Version :   0.1.0
@Desc    :   None
'''


from core import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
