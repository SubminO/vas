FROM python:3.7-alpine

RUN adduser -D vas

WORKDIR /home/vas

COPY prod_requirements.txt requirements.txt

RUN apk add --no-cache mariadb-dev build-base

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN apk update
RUN pip install --upgrade pip \
  && pip install -r requirements.txt \
  && pip install gunicorn
#  && pip install pymysql
#  && pip install mysqlclient \
#  && rm -rf .cache/pip \
#  && apk del build-dependencies

#COPY app app
COPY boot.sh boot.sh
#COPY migrations migrations
#COPY otsmgps.py config.py boot.sh ./
#RUN flask translate init
#RUN flask translate update
RUN chmod +x boot.sh

#ENV FLASK_APP otsmgps.py

RUN chown -R vas:vas ./
USER vas
WORKDIR /home/vas/vas

EXPOSE 8000
ENTRYPOINT ["../boot.sh"]
#CMD ["gunicorn"  , "-b", "8000", "--access-logfile", "-", "--error-logfile", "-", "-w", "5", "mysite/mysite.wsgi:application"]