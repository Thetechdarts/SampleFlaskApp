FROM python:3.13.0a5-slim-bookworm
WORKDIR /sampleflaskapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python","app.py"]