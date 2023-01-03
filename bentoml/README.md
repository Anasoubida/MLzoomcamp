# MLZOOMCAMP

## BentoML

### Use Bentoml to save a model

In this [notebook](https://github.com/Anasoubida/MLzoomcamp/blob/master/bentoml/train.ipynb) you will find the training of xgboost model to do credit scoring, and we have save it with bentoml.

### Use pydantic to do some data validation

Feel free to discover this part in this [notebook](https://github.com/Anasoubida/MLzoomcamp/blob/master/bentoml/pydantic.ipynb) where you can find a pydantic schema for the data that clients should be sending.

### Use bentoml to import a model, and serve it

**Notice In this homework we used two betnoml models, that uses sklearn, yous can download them from [here](https://github.com/Anasoubida/MLzoomcamp/tree/master/bentoml)**

After downloading the models you can import each model using this command : bentoml models import file_name (in this case your file_name is : coolmodel.bentomodel or coolmodel2.bentomodel)
You can check the bentoml models that you have already on your computer, with this command : 
```bash
bentoml models list
```

To see the version of all packages that you have in a bentoml model, run this 
```bash
bentoml models get model_name:tag
```

To serve a model, we will use this script [service.py](https://github.com/Anasoubida/MLzoomcamp/blob/master/bentoml/service.py), and run this command 
```bash
bentoml serve service.py:svc –reload
```

### Locust to generate many client requests
Before starting the locust client testing, you should launch your betnoml service with this command : 
```bash
bentoml serve service.py:svc –reload
```
After that we will use this script [locustfile.py](https://github.com/Anasoubida/MLzoomcamp/blob/master/bentoml/locustfile.py)
Then you can start locust load testing client with:

```bash
locust -H http://localhost:3000
```