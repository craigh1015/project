FROM python:3.9-slim

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY app.py /app
COPY static/* /app/static/

EXPOSE 8080

ENV PORT 8080

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app
