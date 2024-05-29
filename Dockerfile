FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

COPY ./.env /app/.env

RUN python /app/scripts/download_models.py

CMD ["python", "main.py"]