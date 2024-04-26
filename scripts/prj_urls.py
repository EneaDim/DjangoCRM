import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-prj", "--prj", type=str, required='True', 
					help="Define the name of the project")
    args = vars(ap.parse_args())
    prj = args.get("prj")
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during ARGUMENT PASSING:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()

prj_urls_file = str(prj)+'/urls.py'
f = open(prj_urls_file, 'w+')
mystr = "from django.contrib import admin\n"
mystr += "from django.urls import path, include\n\n"
mystr += "urlpatterns = [\n"
mystr += "    path('admin/', admin.site.urls),\n"
mystr += "    path('', include('"+str(prj)+"_website.urls')),\n"
mystr += "]\n"
f.write(mystr)
f.close()
