#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from .app import capp

__author__ = "Abhilash Joseph C"
__version__ = "v2.2018.07.13"

@capp.task
def add(x, y):
    return x + y