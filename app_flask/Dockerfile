FROM bitnami/python:3.8.13

RUN pip install elasticsearch
RUN pip install flask
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
COPY . .
CMD ["flask", "run"]