FROM python:3.7
ADD . /tmp
WORKDIR /app
COPY requirment.txt requirment.txt
RUN pip install -r requirment.txt

COPY flaskapp.py flaskapp.py
COPY publisher.py publisher.py

CMD ["python", "flaskapp.py"]
