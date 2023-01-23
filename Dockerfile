FROM python:3.10.2 
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

#FEWRCC FEW Remote Control Cars
#From Base Image
#Port number 
#Copy Image from where
#Run these commands
#copy image {source: desination}
#Command ["String Commands"]