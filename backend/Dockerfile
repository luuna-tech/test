FROM python:3.8
COPY requirements.txt .
WORKDIR /app
RUN pip install -r requirements.txt
COPY src/ .
CMD [ "python", "./server.py" ]