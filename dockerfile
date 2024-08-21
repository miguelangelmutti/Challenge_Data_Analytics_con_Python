FROM python:3.12

LABEL author="miguemutti1989"

WORKDIR /home/miguehp/Documentos/Challenge_Data_Analytics_con_Python_Docker/app

COPY . /home/miguehp/Documentos/Challenge_Data_Analytics_con_Python_Docker/app/

RUN pip install -r requirements.txt

CMD [ "python","main.py" ]