FROM python:3.12.0b1

ADD requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

ADD . /src
WORKDIR /src
CMD python inject_articles.py; python app.py
