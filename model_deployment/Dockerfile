FROM svizor/zoomcamp-model:3.9.12-slim
# add your stuff here

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["predict.py","send_request.py","model1.bin","dv.bin","./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve","--listen=0.0.0.0:9696","predict:app"]
