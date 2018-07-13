#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from celery import Celery
__author__ = "Abhilash Joseph C"
__version__ = "v2.2018.07.13"


capp = Celery(__name__, broker='pyamqp://guest@localhost//')

capp.conf.update(
    {
        'imports': ['celery_app.tasks']
    }
)