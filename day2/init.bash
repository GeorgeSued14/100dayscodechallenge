#!/bin/bash

export FLASK_APP=main.py
printenv FLASK_APP
export FLASK_ENV=development
printenv FLASK_ENV
flask run