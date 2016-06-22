from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError

from .models import(DBSession,  User,  Collection,  Book,  Film, History, Access)
from pyramid.httpexceptions import(HTTPFound,  HTTPNotFound)
from pyramid.view import(view_config,  forbidden_view_config)
from pyramid.security import(remember,  forget)
from .security import USERS

@view_config(route_name='index', renderer='myproject/templates/index.jinja2')
def index(request):
   if request.authenticated_userid == "admin":
    	return {'username': request.authenticated_userid, 'project': 'Myproject'}
   return {'project': 'Myproject'}

@view_config(route_name='bookPage', renderer='myproject/templates/bookPage.jinja2')
def bookPage(request):
    if request.authenticated_userid == "admin":
    	return {'username': request.authenticated_userid, 'project': ''}
    return {'project': 'Myproject'}

@view_config(route_name='filmPage', renderer='myproject/templates/filmPage.jinja2')
def filmPage(request):
    return {'username': request.authenticated_userid, 'project': 'Myproject'}

@view_config(route_name='historyPage', renderer='myproject/templates/historyPage.jinja2')
def historyPage(request):
    if request.authenticated_userid == "admin":
    	return {'username': request.authenticated_userid, 'project': ''}
    return {'project': 'Myproject'}



conn_err_msg = """\
You have problem!
"""

@view_config(route_name='login', renderer='myproject/templates/avtorization.jinja2')
@forbidden_view_config(renderer='myproject/templates/avtorization.jinja2')
def login(request):
    	if 'submitted' in request.params:
        	login = request.params['login']
        	password = request.params['password']
		if USERS.get(login) == password:
		    	headers = remember(request, login)			
            		return HTTPFound(location = 'home', headers = headers)
        	else:
    			return {'message': "Incorrect login or password", 'project': 'Myproject'}
	return {'project': 'Myproject'}

	
@view_config(route_name='logout')
def logout(request):
	headers = forget(request)
	return HTTPFound(location = request.referrer,
headers = headers)
