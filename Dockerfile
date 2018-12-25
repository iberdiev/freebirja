# freebirja
# Version: 1.0

FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /freebirja
WORKDIR /freebirja
ADD . /freebirja/
#COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python manage.py migrate
# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]


# docker build -t freebirja_image . 
# docker run --name webapp -p 8000:8000 freebirja_image
# docker rm $(docker ps -a -q -f status=exited)

