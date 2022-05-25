FROM bitnami/python:3.8.13

RUN pip install elasticsearch
COPY  . .

CMD [ "python", "busqueda.py" ]