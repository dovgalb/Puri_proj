FROM python:3.9.6-alpine

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /backend/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /backend/requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /backend/entrypoint.sh
RUN chmod +x /backend/entrypoint.sh

COPY . .

ENTRYPOINT ["sh", "/backend/entrypoint.sh"]
