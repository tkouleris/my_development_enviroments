FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    pkg-config \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--debug"]