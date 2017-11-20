#!/bin/bash
cd ..
export FLASK_APP=EuclideanMetric.py
export FLASK_DEBUG=true
flask run --host=0.0.0.0 --port=8080
