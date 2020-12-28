FROM python

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY server.py /app

EXPOSE 5000

CMD [ "python", "server.py" ]
