FROM jupyter/pyspark-notebook:latest

COPY PySpark/main.py /home/jovyan/main.py

CMD ["spark-submit", "--master", "local", "/home/jovyan/main.py"]
