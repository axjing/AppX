#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   tasks.py
@Time    :   2023/10/25 21:11:16
@Author  :   axjing 
@Version :   0.1.0
@Desc    :   None
'''

from core.celery_app import celery_app


@celery_app.task(acks_late=True)
def example_task(word: str) -> str:
    return f"test task returns {word}"
