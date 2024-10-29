FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN apt-get -y update && apt-get -y install net-tools iputils-ping curl
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
