FROM python:3.9.1-alpine
ADD . /code
WORKDIR /code
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
