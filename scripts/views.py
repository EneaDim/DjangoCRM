import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-prj", "--prj", type=str, required='True', 
					help="Define the name of the project")
    ap.add_argument("-methods", "--methods", type=str, required='True', 
					help="Define the methods of the application")
    ap.add_argument("-log_type", "--log_type", type=str, required='True', 
					help="Define the methods of the application")
    args = vars(ap.parse_args())
    prj = args.get("prj")
    methods = args.get("methods")
    log_type = args.get("log_type")
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during ARGUMENT PASSING:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()

# FILE
prj_methods_file = str(prj)+'_website/views.py'

# STRING -> LIST
methods = methods.split()

# DEFINE METHODS
basic = "def home(request):\n"
basic += "	#records = Record.objects.all()\n"
basic += "	# Check to see if logging in\n"
if log_type == 'basic':
    basic += "	if request.method == 'POST':\n"
    basic += "		username = request.POST['username']\n"
    basic += "		password = request.POST['password']\n"
    basic += "		# Authenticate\n"
    basic += "		user = authenticate(request, username=username, password=password)\n"
    basic += "		if user is not None:\n"
    basic += "			login(request, user)\n"
    basic += '			messages.success(request, "You Have Been Logged In!")\n'
    basic += "			return redirect('home')\n"
    basic += "		else:\n"
    basic += '			messages.success(request, "There Was An Error Logging In, Please Try Again...")\n'
    basic += "			return redirect('home')\n"
    basic += "	else:\n"
    basic += "		return render(request, 'home.html', {})\n"
else:
    basic += "	return render(request, 'home.html', {})\n"

logout = 'def logout_user(request):\n'
logout += '	logout(request)\n'
logout += '	messages.success(request, "You Have Been Logged Out...")\n'
logout += "	return redirect('home')\n"



# POSSIBLE METHODS TO ADD
my_dict = { 'basic' : basic,
			'logout': logout
}

# WRITE FILE
f = open(prj_methods_file, 'w+')
mystr = 'from django.shortcuts import render, redirect\n'
mystr += 'from django.contrib.auth import authenticate, login, logout\n'
mystr += 'from django.contrib import messages\n\n'
for key in methods:
	if key in my_dict:
		mystr += my_dict[key]+"\n"
f.write(mystr)
f.close()
