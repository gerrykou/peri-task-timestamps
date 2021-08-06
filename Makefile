clean:
	rm -rf venv

install:clean
	( \
	   python3 -m venv venv; \
       venv/bin/python -m pip install -r requirements.txt; \
    )

run:
	venv/bin/python src/app.py --period=1h --tz=Europe/Athens --t1=20210714T204603Z --t2=20210715T123456Z

run-all:
	( \
	   venv/bin/python src/app.py --period=1h --tz=Europe/Athens --t1=20210714T204603Z --t2=20210715T123456Z; \
       venv/bin/python src/app.py --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z; \
	   venv/bin/python src/app.py --period=1mo --tz=Europe/Athens --t1=20210214T204603Z --t2=20211115T123456Z; \
	   venv/bin/python src/app.py --period=1y --tz=Europe/Athens --t1=20180214T204603Z --t2=20211115T123456Z; \
	   venv/bin/python src/app.py --period=1w --tz=Europe/Athens --t1=20180214T204603Z --t2=20211115T123456Z; \
	   # venv/bin/python src/app.py --period=1h --tz=Europe/Athes --t1=20211115T123456Z --t2=20211010T204603Z; \
	   # venv/bin/python src/app.py --period=1w --tz=Europe/Athens --t1=20180214T204603Z --t2=20211115T123456Z; \
    )
	
run-test:
		venv/bin/python -m unittest test.test_app.TestApp.test_datetime_obj2string

run-error:
	venv/bin/python src/app.py --period=1h --tz=Europe/Athens --t1=20211115T123456Z --t2=20211010T204603Z