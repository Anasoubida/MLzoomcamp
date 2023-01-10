# MLZOOMCAMP

## Serverless

### TFLITE

In this homework we will use AWS lambda function to serve our model that we've created in the previous week, for dino or dragon classification.

We have saved our model in tflite format, it is a format that is used usualy in production to serve tensorflow models. You can check that in this [notebook](https://github.com/Anasoubida/MLzoomcamp/blob/master/serverless/converting_to_tflite.ipynb)

The model is called **dino_dragon_10_0.899.tflite**

### Predict with tflite model and lambda function

[Here](https://github.com/Anasoubida/MLzoomcamp/blob/master/serverless/predict_tflite.py) I created the code to do predictions with the tflite model, and i added the code for lambda function

### Docker image

I used docker image that contains the tflite model and this [script](https://github.com/Anasoubida/MLzoomcamp/blob/master/serverless/predict_tflite.py)

To build this docker image run the following command : 

```bash
docker build -t image_name .
```

To run the docker image run the following command :

```bash
docker run -it --rm -p 8080:8080 dino_dragon
```

After running the previous command you can test your service locally using this [code](https://github.com/Anasoubida/MLzoomcamp/blob/master/serverless/test.py)

### How to push a docker image to ecr

#### 1) First of all you should install awscli to comunicate with aws

```bash
pip install awscli
```

#### 2) You should configure your aws infos

run this command :
```bash
aws configure
```

To see how to get your **AWS Access key ID** and  **AWS Secret Access Key**, go to this [link](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html)

#### 3) Create the repository 

To do that run this command and replace the image_name by the name of your choice:

```bash
aws ecr create-repository --repository-name {image_name}
```

Don't forget to copy your "repositoryUri", you will need it in the next steps

#### 4)  log in to your repository

Copy the "repositoryUri" without the last part that refers to the name of your image
and replace it in link in this command : 

```bash
aws ecr get-login-password | docker login --username AWS --password-stdin {link}/reponame
```

#### 5) tag your docker image

replace the name of your image in {image_name}, the {repositoryUri} by your repositoryUri, {tag} by the tag that you want
and run this command

```bash
docker tag {image_name}:latest {repositoryUri}:{tag_name} 
```

#### 6) Push your docker image to ecr

run this command

```bash
docker push {repositoryUri}:{tag_name}
```

To check if your image was pushed succesfully go to ecr, and refresh the page

** NB : To create the lambda function in aws, and the rest API go follow the steps that Alexey explains in those two videos : ** 
[Creating the Lambda Function](https://www.youtube.com/watch?v=kBch5oD5BkY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=94)
[API Gateway: Exposing the Lambda Function](https://www.youtube.com/watch?v=wyZ9aqQOXvs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=95)
