clean:
	@find . -name "*.pyc" -exec rm -f {} \;

bootstrap:
	@pip install -r requirements.txt

test:
	@specloud --nocapture --verbose --where=tests --with-coverage --cover-package=dojomap --cover-erase --with-gae --gae-application=.
