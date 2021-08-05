clean:
	rm -rf venv

install:clean
	( \
	   python3 -m venv venv; \
       venv/bin/python -m pip install -r requirements.txt; \
    )

run:
	venv/bin/python src/app --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z -v
	

	
