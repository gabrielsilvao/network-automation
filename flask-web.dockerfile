FROM python
MAINTAINER Gabriel Silva
COPY . /var/www
WORKDIR /var/www
RUN pip install flask
CMD ["python","app.py"]