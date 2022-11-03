# MLZOOMCAMP 
## MODEL DEPLOYMENT

Here we are using a model for churn prediction. First of all, install pipenv with this command : pip install pipenv and after that, you can install the virtual env on your local machine if you want, using this command : pipenv install

Our model was trained on this data, if you want to retrain the model feel free to use the code train.py and adapt it if you want :)

We have saved the model and the DictVectorizer into bin files, using Pickle. So you can load those files, to do predictions and score new clients. To do that you can use this script predict_locally.

### Score clients using the web service

run this command on your cmd

waitress-serve --listen=0.0.0.0:9696 predict:app

And after that, you can run this script : send_request.py, feel free to do changes on tha variables values of the client !

### Deploy the web service with docker
You should build the docker image, using this command

docker build -t churn_service .

And then you can run the web service into the docker container 

docker run -it -p 9696:9696 churn_service:latest

Now you can run this script : send_request.py to score any client you want !
