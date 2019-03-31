FROM python:alpine
LABEL maintainer="r3ap3rpy"
RUN pip install flask
COPY app.py app.py
EXPOSE 9999
ENTRYPOINT ["python", "app.py"]