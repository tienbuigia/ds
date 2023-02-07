FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-dev python3-venv python3-pip
WORKDIR /app
COPY . .
# create and active virtual env
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r requirements.txt
CMD ["python"]
EXPOSE 5555
