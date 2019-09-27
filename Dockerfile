FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install python3-markdown

COPY . .

CMD [ "python3", "./run.py" ]
