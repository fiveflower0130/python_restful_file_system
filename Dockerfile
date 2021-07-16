FROM python:3.8-slim-buster
WORKDIR /python_flask
ADD . /python_flask
RUN pip3 install -r requirements.txt
CMD ["python3", "run.py"]