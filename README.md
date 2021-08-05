# Periodic tasks timestamps

docker build -t peri-task-timestamps .

docker run --rm -ti gerrykou/peri-task-timestamps bash -c "cd src;./app.py --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z -v"

https://hub.docker.com/repository/docker/gerrykou/peri-task-timestamps

# Run Tests
python -m unittest test_app.TestApp.test_parse_args