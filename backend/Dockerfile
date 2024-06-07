FROM python:3.11.9-bookworm

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./api api

CMD ["fastapi", "run", "api/main.py"]
