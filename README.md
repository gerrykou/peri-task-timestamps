# Periodic tasks timestamps
```shell_

                 _   _            _    
 _ __   ___ _ __(_) | |_ __ _ ___| | __
| '_ \ / _ \ '__| | | __/ _` / __| |/ /
| |_) |  __/ |  | | | || (_| \__ \   <
| .__/ \___|_|  |_|  \__\__,_|___/_|\_\
|_|
 _   _                     _
| |_(_)_ __ ___   ___  ___| |_ __ _ _ __ ___  _ __  ___
| __| | '_ ` _ \ / _ \/ __| __/ _` | '_ ` _ \| '_ \/ __|
| |_| | | | | | |  __/\__ \ || (_| | | | | | | |_) \__ \
 \__|_|_| |_| |_|\___||___/\__\__,_|_| |_| |_| .__/|___/
                                             |_|

usage: app.py [-h] --period  --t1  --t2  --tz

Print periodic tasks timestamps

optional arguments:
  -h, --help  show this help message and exit
  --period    The supported periods are: 1h, 1d, 1mo, 1y.
  --t1        t1 in UTC with seconds accuracy, in the following form:
              20060102T150405Z
  --t2        t2 in UTC with seconds accuracy, in the following form:
              20060102T150405Z
  --tz        timezone e.g --tz=Europe/Athens ,see
              http://pytz.sourceforge.net/ and
              https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
```
## Run in Docker container - pull image from DockerHub
```shell
docker run --rm -ti gerrykou/peri-task-timestamps bash -c "app.py --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z"
```
https://hub.docker.com/repository/docker/gerrykou/peri-task-timestamps

## Build Docker image and run
```shell
docker build -t peri-task-timestamps .
docker run --rm -ti peri-task-timestamps bash -c "app.py --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z"
```

## Run in Virtualenvironment
```shell
python3 -m venv venv
venv/bin/python -m pip install -r requirements.txt
venv/bin/python src/app.py --period=1h --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z   
venv/bin/python -m unittest discover test
venv/bin/python -m unittest test.test_app.TestApp.test_datetime_obj2string
```

## Run in Linux with make file
```shell
make install  
make run  
make run-all  
make run-test
make run-one-test
```

## Run in Linux
in shell in the /src run : 
```shell
export PATH=$PATH:$(pwd)   
chmod +x src/app.py  
python3 -m pip install -r requirements.txt  
app.py --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z
```

## Run in WSL
See Run in Linux, run after export PATH:  

```shell
dos2unix src/app.py  
```

## Run Tests
```shell
python -m unittest test.test_app.TestApp.test_datetime_obj2string
```
