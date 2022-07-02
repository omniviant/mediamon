FROM python:3.10
RUN apt-get update -qq && apt-get -y install \
        ffmpeg
RUN mkdir /app
ADD src/. /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "mediamonitor.py"]