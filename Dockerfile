FROM python:3.12

RUN mkdir /operator_statistics

WORKDIR /operator_statistics

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD cd statistics_project && gunicorn statistics_project.wsgi:application  --bind 0.0.0.0:80