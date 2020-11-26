FROM python:3.8-alpine
RUN mkdir -p /opt/apps/sofomoapp/src
WORKDIR /opt/apps/sofomoapp/src
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

COPY . /opt/apps/sofomoapp/src
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--chdir", "sofomoapp", "--bind", ":8000", "sofomoapp.wsgi:application"]


