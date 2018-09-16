FROM python:3.6
RUN mkdir /opt/app
RUN mkdir -p /tmp/pipeline/prep_data
RUN mkdir -p /tmp/pipeline/in_data
RUN mkdir -p /tmp/pipeline/out_data
COPY report_api.py report_api.py
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install vim
RUN pip install -r requirements.txt
CMD ["python","report_api.py"]
