FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt --upgrade --no-cache-dir
EXPOSE 80
ENV NAME Stud
CMD ["python", "app.py"]