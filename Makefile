clean:
	@echo 'Cleaning...'
	@find . -name "*.pyc" -exec rm -f {} \;
	@echo 'Done.'

bootstrap:
	@pip install -r requirements.txt

test: clean
	@specloud --nocapture --verbose --where=tests --with-coverage --cover-package=dojomap --cover-erase --with-gae --gae-application=.

lib: update_werkzeug update_jinja2 update_flask update_flask_wtf update_wtforms

update_werkzeug: deps_dir
	@echo 'Updating Werkzeug...'
	@pip install Werkzeug==0.6.1 --download=deps --no-dependencies
	@cd deps && tar -xzvf Werkzeug-0.6.1.tar.gz
	@cp -r deps/Werkzeug-0.6.1/werkzeug libs/
	@rm -rf deps/Werkzeug*
	@echo 'Done.'

update_jinja2: deps_dir
	@echo 'Updating Jinja2...'
	@pip install Jinja2==2.5.5 -d deps --no-dependencies
	@cd deps && tar -xzvf Jinja2-2.5.5.tar.gz
	@cp -r deps/Jinja2-2.5.5/jinja2 libs/
	@rm -rf deps/Jinja2*
	@echo 'Done.'

update_flask: deps_dir
	@echo 'Updating Flask...'
	@pip install Flask==0.6.1 -d deps --no-dependencies
	@cd deps && tar -xzvf Flask-0.6.1.tar.gz
	@cp -r deps/Flask-0.6.1/flask libs/
	@rm -rf deps/Flask*
	@echo 'Done.'

update_wtforms: deps_dir
	@echo 'Updating WTForms...'
	@pip install WTForms==0.6.2 -d deps --no-dependencies
	@cd deps && unzip WTForms-0.6.2.zip
	@cp -r deps/WTForms-0.6.2/wtforms libs/
	@rm -rf deps/WTForms-*
	@echo 'Done.'

update_flask_wtf: deps_dir
	@echo 'Updating Flask-WTF...'
	@pip install Flask-WTF==0.5.2 -d deps --no-dependencies
	@cd deps && tar -xzvf Flask-WTF-0.5.2.tar.gz
	@cp -r deps/Flask-WTF*/flaskext libs/
	@rm -rf deps/Flask-WTF-*
	@echo 'Done.'

deps_dir:
	@test -d deps || mkdir deps
	@test -d libs || mkdir libs
