FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

#FEWRCC FEW Remote Control Cars
#From Base Image
#Port number 
#Copy Image from where
#Run these commands #pip install -r requirements.txt
#copy image {source: desination}
#Command ["String Commands"]