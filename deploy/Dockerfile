FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /gallery/
COPY /src /gallery/src/
COPY deploy/requirements.txt /gallery/requirements.txt
RUN pip install -r requirements.txt
COPY /src /gallery/src
