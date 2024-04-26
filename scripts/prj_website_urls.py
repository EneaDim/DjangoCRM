import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-prj", "--prj", type=str, required='True', 
					help="Define the name of the project")
    ap.add_argument("-web_urls", "--web_urls", type=str, required='True', 
					help="Define the urls related to the features of the application")
    args = vars(ap.parse_args())
    prj = args.get("prj")
    web_urls = args.get("web_urls")
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during ARGUMENT PASSING:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()

# FILE
prj_web_urls_file = str(prj)+'_website/urls.py'

# STRING -> LIST
web_urls = web_urls.split()

# POSSIBLE URLS TO ADD
my_dict = { 'basic' : "path('', views.home, name='home'),",
			'login' : "path('login/', views.login_user, name='login'),", # MOSTLY DONE IN "basic"
			'logout': "path('logout/', views.logout_user, name='logout'),",
			'register' : "path('register/', views.register_user, name='register'),",
			'record' : "path('record/<int:pk>', views.customer_record, name='record'),",
			'delete_record' : "path('delete_record/<int:pk>', views.delete_record, name='delete_record'),",
			'add_record' : "path('add_record/', views.add_record, name='add_record'),",
			'update_record' : "path('update_record/<int:pk>', views.update_record, name='update_record'),"
}

# WRITE FILE
f = open(prj_web_urls_file, 'w+')
mystr = "from django.contrib import admin\n"
mystr += "from django.urls import path, include\n"
mystr += "from . import views\n\n"
mystr += "urlpatterns = [\n"
for key in web_urls:
	if key in my_dict:
		mystr += "    "+str(my_dict[key])+"\n"
mystr += "]\n"
f.write(mystr)
f.close()
