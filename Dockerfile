FROM python:3.9.19-slim-bullseye
COPY . /
RUN pip install -r requirements.txt
CMD ["python", "app.py"]