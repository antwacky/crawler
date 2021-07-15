FROM python:3.7.7-alpine3.12

RUN addgroup -g 10066 -S crawler \
 && adduser -u 10066 -S crawler -G crawler

RUN mkdir -p /var/src/crawler
COPY requirements.txt /var/src/crawler/requirements.txt
COPY *.py /var/src/crawler

RUN chown -R crawler:crawler /var/src/crawler
RUN chmod -R 750 /var/src/crawler

RUN apk add gcc musl-dev libffi-dev \
 && pip install -r /var/src/crawler/requirements.txt \
 && apk del gcc musl-dev libffi-dev

USER crawler

WORKDIR '/var/src/crawler'
ENTRYPOINT [ "python", "/var/src/crawler" ]
