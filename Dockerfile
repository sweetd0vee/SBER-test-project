FROM python:3.9

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# create directories
RUN mkdir /python/
RUN mkdir /python/data

# copy directories
COPY data /python/data

# copy files
COPY base_logger.py /python/base_logger.py
COPY app.py /python/app.py

WORKDIR /python/

EXPOSE 8000

ENTRYPOINT ["uvicorn", "--host",  "0.0.0.0", "--port",  "8000", "app:app"]
