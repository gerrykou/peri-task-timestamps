# Periodic tasks timestamps

## Run in Docker container - pull image from DockerHub
docker run --rm -ti gerrykou/peri-task-timestamps bash -c "app --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z -v"

https://hub.docker.com/repository/docker/gerrykou/peri-task-timestamps

## Run in Virtualenvironment
make install
make run

## Run locally
in shell in the /src run :
export PATH=$PATH:$(pwd)
python3 -m pip install -r requirements.txt
app --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z -v

## Build Docker image
docker build -t peri-task-timestamps .

## Run Tests
python -m unittest test_app.TestApp.test_parse_args