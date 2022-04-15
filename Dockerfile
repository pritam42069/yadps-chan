FROM python:3.10
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python -m pip install --editable .
COPY . .
CMD [ "python", "main.py" ]