import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-prj", "--prj", type=str, required='True', 
					help="Define the name of the project")
    ap.add_argument("-navbar", "--navbar", type=str, required='True', 
					help="Define the type of navbar")
    args = vars(ap.parse_args())
    prj = args.get("prj")
    navbar = args.get("navbar")
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during ARGUMENT PASSING:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()

# NAVBAR
if not navbar == '':
	html_navbar_file = str(prj)+'_website/templates/'+str(prj)+'/navbar.html'
	f = open(html_navbar_file, 'w+')
	if navbar == 'basic':
		mystr = '<nav class="navbar navbar-expand-lg navbar-dark bg-dark">\n'
		mystr += '  <div class="container-fluid">\n'
		mystr += '    <a class="navbar-brand" href="#">Django CRM</a>\n'
		mystr += '    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\n'
		mystr += '      <span class="navbar-toggler-icon"></span>\n'
		mystr += '    </button>\n'
		mystr += '    <div class="collapse navbar-collapse" id="navbarSupportedContent">\n'
		mystr += '      <ul class="navbar-nav me-auto mb-2 mb-lg-0">\n'
		mystr += '        <li class="nav-item">\n'
		mystr += '          <a class="nav-link active" aria-current="page" href="#">Home</a>\n'
		mystr += '        </li>\n'
		mystr += '        <li class="nav-item">\n'
		mystr += '          <a class="nav-link" href="#">Link</a>\n'
		mystr += '        </li>\n'
		mystr += '        <li class="nav-item dropdown">\n'
		mystr += '          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">\n'
		mystr += '            Dropdown\n'
		mystr += '          </a>\n'
		mystr += '          <ul class="dropdown-menu">\n'
		mystr += '            <li><a class="dropdown-item" href="#">Action</a></li>\n'
		mystr += '            <li><a class="dropdown-item" href="#">Another action</a></li>\n'
		mystr += '            <li><hr class="dropdown-divider"></li>\n'
		mystr += '            <li><a class="dropdown-item" href="#">Something else here</a></li>\n'
		mystr += '          </ul>\n'
		mystr += '        </li>\n'
		mystr += '        <li class="nav-item">\n'
		mystr += '          <a class="nav-link disabled" aria-disabled="true">Disabled</a>\n'
		mystr += '        </li>\n'
		mystr += '      </ul>\n'
		mystr += '      <form class="d-flex" role="search">\n'
		mystr += '        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">\n'
		mystr += '        <button class="btn btn-outline-success" type="submit">Search</button>\n'
		mystr += '      </form>\n'
		mystr += '    </div>\n'
		mystr += '  </div>\n'
		mystr += '</nav>\n'
	else:
		raise Exception('\033[93m\nSelect a proper navbar between:\n\t-basic\n\033[0m')
	f.write(mystr)
	f.close()

#BASE
html_base_file = str(prj)+'_website/templates/'+str(prj)+'/base.html'
# WRITE FILE
f = open(html_base_file, 'w+')
mystr = '<!doctype html>\n'
mystr += '<html lang="en">\n'
mystr += '  <head>\n'
mystr += '    <meta charset="utf-8">\n'
mystr += '    <meta name="viewport" content="width=device-width, initial-scale=1">\n'
mystr += '    <title>Django CRM</title>\n'
mystr += '    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">\n'
mystr += '  </head>\n'
mystr += '  <body>\n'
if not navbar == '':
	mystr += "    {% include 'navbar.html' %}\n"
mystr += '    <div class="container">\n'
mystr += '      <br/>\n'
mystr += '      {% if messages %}\n'
mystr += '        {% for message in messages %}\n'
mystr += '          <div class="alert alert-warning alert-dismissible fade show" role="alert">\n'
mystr += '            {{ message }}\n'
mystr += '            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n'
mystr += '          </div>\n'
mystr += '        {% endfor %}\n'
mystr += '      {% endif %}\n'
mystr += '      \n'
mystr += '      {% block content %}\n'
mystr += '      {% endblock%}\n'
mystr += '    </div>\n'
mystr += '\n'
mystr += '    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>\n'
mystr += '  </body>\n'
mystr += '</html>\n'
f.write(mystr)
f.close()

#HOME
html_home_file = str(prj)+'_website/templates/'+str(prj)+'/home.html'
f = open(html_home_file, 'w+')
mystr = "{% extends 'base.html' %}\n"
mystr += '{% block content %}\n'
mystr += '{% if user.is_authenticated %}\n'
#mystr += '<table class="table table-striped table-hover table-bordered">\n'
#mystr += '  <thead class="table-dark">\n'
#mystr += '    <tr>\n'
#mystr += '      <th scope="col">Name</th>\n'
#mystr += '      <th scope="col">Email</th>\n'
#mystr += '      <th scope="col">Phone</th>\n'
#mystr += '      <th scope="col">Address</th>\n'
#mystr += '      <th scope="col">City</th>\n'
#mystr += '      <th scope="col">State</th>\n'
#mystr += '      <th scope="col">Zipcode</th>\n'
#mystr += '      <th scope="col">Created At</th>\n'
#mystr += '      <th scope="col">ID</th>\n'
#mystr += '    </tr>\n'
#mystr += '  </thead>\n'
#mystr += '  <tbody>\n'
#mystr += '{% if records %}\n'
#mystr += '	{% for record in records %}\n'
#mystr += '		<tr>\n'
#mystr += '			<td>{{ record.first_name }} {{ record.last_name }}</td>\n'
#mystr += '			<td>{{ record.email }}</td>\n'
#mystr += '			<td>{{ record.phone }}</td>\n'
#mystr += '			<td>{{ record.address }}</td>\n'
#mystr += '			<td>{{ record.city }}</td>\n'
#mystr += '			<td>{{ record.state }}</td>\n'
#mystr += '			<td>{{ record.zipcode }}</td>\n'
#mystr += '			<td>{{ record.created_at }}</td>\n'
#mystr += '			<td><a href='+"{% url 'record' record.id %}"+'">{{ record.id }}</a></td>\n'
#mystr += '		</tr>\n'
#mystr += '	{% endfor %}\n'
#mystr += '{% endif %}\n'
#mystr += '	  </tbody>\n'
#mystr += '	</table>\n'
mystr += '{% else %}\n'
mystr += '<div class="col-md-6 offset-md-3">\n'
mystr += '<h1>Login</h1>\n'
mystr += '<br/>\n'
mystr += '<form method="POST" action="'+"{% url 'home' %}"+'>\n'
mystr += '	{% csrf_token %}\n'
mystr += '  <div class="mb-3">\n'
mystr += '    <input type="text" class="form-control" name="username", placeholder="Username" required>\n'
mystr += '  </div><br/>\n'
mystr += '  <div class="mb-3">\n'
mystr += '    <input type="password" class="form-control" name="password", placeholder="Password" required>\n'
mystr += '  </div>\n'
mystr += '  <br/>\n'
mystr += '  <button type="submit" class="btn btn-secondary">Login</button>\n'
mystr += '</form>\n'
mystr += '{% endif %}\n'
mystr += '{% endblock %}\n'
f.write(mystr)
f.close()
