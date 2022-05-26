FROM bitnami/python:3.8.13

WORKDIR /path/to/

COPY certs.pem /path/to/

RUN pip install elasticsearch
RUN pip install urllib3==1.23

COPY . .

CMD [ "python", "busqueda.py" ]