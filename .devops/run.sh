#!/bin/bash

flask db upgrade
gunicorn -w 4 "run:app"
