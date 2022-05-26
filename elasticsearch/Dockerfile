FROM elasticsearch:8.2.1

RUN network create elastic
RUN -d --name elasticsearch --net elastic -p 9200:9200 elasticsearch:tag
