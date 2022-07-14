FROM python:3.8
LABEL maintainer="Fady Refaat"

COPY . /techtrends
ADD /techtrends /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python init_db.py

EXPOSE 3111
# command to run on container start
CMD [ "python", "app.py" ]
