FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app
WORKDIR /app
COPY . /app
EXPOSE 8000
RUN pip install --requirement requirements.txt
CMD ["python3", "manage.py", "runserver"]
