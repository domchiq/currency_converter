#get official python runtime as parent
FROM python:3.6.8-slim-jessie

#set working directory
WORKDIR /app

#copy all files from current directory to working directory
COPY . /app

#install all dependencies
RUN pip3 install -r /app/requirements.txt

#set the port to be used
EXPOSE 80

#run the app when container starts
CMD ["python3", "WEB_Converter.py"]