FROM python:3.7
ADD . /tmp
WORKDIR /app
COPY requirment.txt requirment.txt
RUN pip install -r requirment.txt

COPY consumer.py consumer.py
COPY dbds.py dbds.py
CMD ["python", "consumer.py"]
