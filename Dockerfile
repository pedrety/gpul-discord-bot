FROM python:3
LABEL Author="Bruno Cabado <bruno.cabado@gpul.org>"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]