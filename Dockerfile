FROM python:3
COPY requirements.txt /cycle-class-generator/requirements.txt
WORKDIR /cycle-class-generator
RUN pip3 install -r requirements.txt

#expose Postgres port
EXPOSE 5432
