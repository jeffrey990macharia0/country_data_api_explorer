FROM python:3.6-slim

COPY . /Docker_py

WORKDIR /Docker_py

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python"]

EXPOSE 5000

CMD ["app.py"]
