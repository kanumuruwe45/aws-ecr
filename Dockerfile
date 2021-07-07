
FROM python:2.7-alpine3.9
COPY . /app
WORKDIR /app
RUN pip install Flask
EXPOSE 5000
CMD ["python","app.py"]