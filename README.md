# Periodic tasks timestamps

## Run in Docker container - pull image from DockerHub
docker run --rm -ti gerrykou/peri-task-timestamps bash -c "app.py --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z"

https://hub.docker.com/repository/docker/gerrykou/peri-task-timestamps

## Run in Virtualenvironment
python3 -m venv venv
venv/bin/python -m pip install -r requirements.txt
venv/bin/python src/app.py --period=1h --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z   
venv/bin/python -m unittest test.test_app.TestApp.test_datetime_obj2string

## Run in Linux with make file
make install  
make run  
make run-all  
make run-test

## Run in Linux
in shell in the /src run :  
export PATH=$PATH:$(pwd)   
chmod +x src/app.py  
python3 -m pip install -r requirements.txt  
app.py --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z

## Run in WSL
See Run in Linux, run after export PATH:  

dos2unix src/app.py  


## Build Docker image
docker build -t peri-task-timestamps .

## Run Tests
python -m unittest test.test_app.TestApp.test_datetime_obj2string
