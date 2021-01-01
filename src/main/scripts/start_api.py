#!/usr/bin/env python

from sys import path
path.append("src/main/python")

from api.backend import app

app.run()
