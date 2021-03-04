#!/bin/bash

export FLASK_APP=app.py
printenv FLASK_APP
export FLASK_ENV=development
printenv FLASK_ENV
flask run