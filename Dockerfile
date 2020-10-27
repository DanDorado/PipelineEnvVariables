FROM python:3.8-alpine

COPY ./envtesting.py /envtest/envtesting.py

WORKDIR /envtest

RUN pip install flask

CMD ["python", "envtesting.py"]