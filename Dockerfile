FROM python:3.6
COPY . /Docker_py
WORKDIR /Docker_py
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
