FROM python:3-slim-buster
WORKDIR /asvs-report
COPY . /asvs-report
RUN pip install -r requirements.txt
ENTRYPOINT ["python","main.py"]
