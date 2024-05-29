FROM python:3.9

ARG BLOB_CONNECTION_STRING
ENV BLOB_CONNECTION_STRING=${BLOB_CONNECTION_STRING}

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python /app/scripts/download_models.py

CMD ["python", "main.py"]