# MAIN PARAMETERS
PROJECT?='crm'
# DATABASE
DB?='mysql'
# URLS and BACKEND
FEATURES?='basic logout'
LOG_TYPE?='basic'
# HTML
NAVBAR?='basic'

init_flow: create start_app db basic_setting super_user

middle_flow: basic_setting urls views html_base run

create:
	django-admin startproject $(PROJECT)

start_app:
	python manage.py start_app $(PROJECT)"_website"

db:
	python scripts/create_db.py -prj $(PROJECT) -db $(DB)
	python mydb.py

super_user:
	python manage.py createsuperuser

run:
	python manage.py runserver

init_github:
	git config --global user.name "EneaDim" ;\
    git config --global user.email "eneadim95@gmail.com" ;\
    git config --global push.default matching ;\
    git config --global alias.co checkout ;\
    git init

basic_setting:
	python scripts/basic_setting.py -prj $(PROJECT) -db $(DB)	

urls: prj_urls prj_web_urls

prj_urls:
	python scripts/prj_urls.py -prj $(PROJECT)

prj_web_urls:
	python scripts/prj_website_urls.py -prj $(PROJECT) -web_urls $(FEATURES)

views:
	python scripts/views.py -prj $(PROJECT) -methods $(FEATURES) -log_type $(LOG_TYPE)

html_base:
	python scripts/html_base.py -prj $(PROJECT) -navbar $(NAVBAR)

