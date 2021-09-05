FROM python:3.7-slim
ENV PYTHONBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host","0.0.0.0", "--port", "8000"]
