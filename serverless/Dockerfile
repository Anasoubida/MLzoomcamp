FROM public.ecr.aws/lambda/python:3.9
COPY predict_tflite.py dino_dragon_10_0.899.tflite .
RUN pip install pillow
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl
CMD ["predict_tflite.lambda_handler"]