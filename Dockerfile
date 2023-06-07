FROM python:3.11.0a6-alpine3.15
WORKDIR /prediction_code
COPY requirements.txt /prediction_code
RUN pip install -r requirements.txt --no-cache-dir
COPY . /prediction_code
CMD python app.py