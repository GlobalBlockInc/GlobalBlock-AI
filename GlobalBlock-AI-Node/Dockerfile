FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    python3 \
    python3-pip \
    curl

RUN git clone https://github.com/ggerganov/llama.cpp.git /app/llama.cpp
WORKDIR /app/llama.cpp
RUN make

RUN pip3 install flask

COPY server.py /app/server.py

EXPOSE 5000

CMD ["python3", "/app/server.py"]
