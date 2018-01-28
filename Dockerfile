FROM python:3.5
RUN apt-get update -y
COPY ./src /app
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /app
RUN pip install -r /tmp/requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
