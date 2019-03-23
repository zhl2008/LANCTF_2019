# -*- coding:utf-8 -*-
from flask import Flask, redirect, request, url_for, make_response

import hashlib

from urllib.parse import unquote_to_bytes


app = Flask(__name__,static_folder="themes")

USERNAME='test'
PASSWORD='test'
SECRET=b'padding'
FLAG_VALUE='LANCTF{a2408ae9b62ec7b02b976f130060892b}'

@app.route("/")
def hello():
	return htmlhello()

@app.route("/login", methods=["POST","GET"])
def login():
	if request.method=="POST":
		username = request.form["username"]
		password = request.form["password"]

		if username != USERNAME or password != PASSWORD:
			return redirect(url_for("hello"))
		else:
			resp = make_response(redirect(url_for("user_page")))
			auth_value = "username={0}&role={1}".format(username, "user").encode()
			sig_value = make_signature(auth_value)
			resp.set_cookie("auth", auth_value)
			resp.set_cookie("sig", sig_value)
			return resp
	else:
		return htmlindex()

@app.route("/user", methods=["GET"])
def user_page():
    auth_cookie = unquote_to_bytes(request.cookies.get("auth"))
    sig_cookie = unquote_to_bytes(request.cookies.get("sig"))

    if auth_cookie is None or sig_cookie is None:
        return redirect(url_for("hello"))

    if sig_cookie != make_signature(auth_cookie):
        resp = make_response(redirect(url_for("hello")))
        resp.delete_cookie("auth")
        resp.delete_cookie("sig")
        return resp

    return "<h1>Hola guset, only admin can reach secret page</h1><br><!--maybe source page helps you-->"


@app.route("/admin", methods=["GET"])
def admin_page():
    auth_cookie = unquote_to_bytes(request.cookies.get("auth"))
    sig_cookie = unquote_to_bytes(request.cookies.get("sig"))

    if auth_cookie is None or sig_cookie is None:
        return redirect(url_for("hello"))

    if sig_cookie != make_signature(auth_cookie):
        
        resp = make_response(redirect(url_for("hello")))
        resp.delete_cookie("auth")
        resp.delete_cookie("sig")
        return resp

    cookie_params = {}
    for p in auth_cookie.split(b"&"):
        key, val = p.split(b"=")
        cookie_params[key] = val

    if cookie_params.get(b"role") == b"admin":
        return FLAG_VALUE
    else:
        return redirect(url_for("user_page"))

@app.route("/source", methods=["GET"])
def source():
	s='SECRET=XXXXXXX'
	s+='''
@app.route("/admin", methods=["GET"])
	def admin_page():
    auth_cookie = unquote_to_bytes(request.cookies.get("auth"))
    sig_cookie = unquote_to_bytes(request.cookies.get("sig"))

    if auth_cookie is None or sig_cookie is None:
        return redirect(url_for("hello"))
    
    if sig_cookie != make_signature(auth_cookie):
        
        resp = make_response(redirect(url_for("hello")))
        resp.delete_cookie("auth")
        resp.delete_cookie("sig")
        return resp

    cookie_params = {}
    for p in auth_cookie.split(b"&"):
        key, val = p.split(b"=")
        cookie_params[key] = val

    if cookie_params.get(b"role") == b"admin":
        return FLAG_VALUE
    else:
        return redirect(url_for("user_page"))

def make_signature(value):
    temp = SECRET + value
    return hashlib.md5(temp).hexdigest().encode()
	'''
	return s

def make_signature(value):
    temp = SECRET + value
    return hashlib.md5(temp).hexdigest().encode()

def htmlindex():
	a='''

<!DOCTYPE html>
<html>
<head>
	<title>LANCTF</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="shortcut icon" href="/themes/core/static/img/favicon.ico"
		  type="image/x-icon">
	<link rel="stylesheet" href="/themes/core/static/css/vendor/bootstrap.min.css">
	<link rel="stylesheet" href="/themes/core/static/css/vendor/font-awesome/fontawesome-fonts.css" type='text/css'>
	<link rel="stylesheet" href="/themes/core/static/css/vendor/font-awesome/fontawesome-all.min.css" type='text/css'>
	<link rel="stylesheet" href="/themes/core/static/css/vendor/font.css"  type='text/css'>
	<link rel="stylesheet" href="/themes/core/static/css/jumbotron.css">
	<link rel="stylesheet" href="/themes/core/static/css/sticky-footer.css">
	<link rel="stylesheet" href="/themes/core/static/css/base.css">
	

	
	<link rel="stylesheet" type="text/css" href="/static/user.css">
	<script src="/themes/core/static/js/vendor/promise-polyfill.min.js"></script>
	<script src="/themes/core/static/js/vendor/fetch.min.js"></script>
	<script src="/themes/core/static/js/CTFd.js"></script>
	<script src="/themes/core/static/js/vendor/moment.min.js"></script>
	<script src="/themes/core/static/js/vendor/nunjucks.min.js"></script>
	<script type="text/javascript">
		var script_root = "";
		var csrf_nonce = "ba980e92a83020d3e7f135d2aa540b3ef64b59aee6c8faba0e4c18800ed413d1";
		var user_mode = "users";
		CTFd.options.urlRoot = script_root;
		CTFd.options.csrfNonce = csrf_nonce;
	</script>
</head>
<body>
	<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
		<div class="container">
			<a href="/" class="navbar-brand">
				
				UnderGroundCityCTF
				
			</a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#base-navbars"
					aria-controls="base-navbars" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="base-navbars">
				<ul class="navbar-nav mr-auto">
					

					<li class="nav-item">
						<a class="nav-link" href="/notifications">Notifications</a>
					</li>
					
						<li class="nav-item">
							<a class="nav-link" href="/users">Users</a>
						</li>
						
					
					
						<li class="nav-item">
							<a class="nav-link" href="/scoreboard">Scoreboard</a>
						</li>
					
					<li class="nav-item">
						<a class="nav-link" href="/challenges">Challenges</a>
					</li>
				</ul>

				<hr class="d-sm-flex d-md-flex d-lg-none">

				<ul class="navbar-nav ml-md-auto d-block d-sm-flex d-md-flex">
					
						
						<li class="nav-item">
							<a class="nav-link" href="/login">Login</a>
						</li>
					
				</ul>
			</div>
		</div>
	</nav>

	<main role="main">
		
<div class="jumbotron">
	<div class="container">
		<h1>Login</h1>
	</div>
</div>
<div class="container">
	<div class="row">
		<div class="col-md-6 offset-md-3">
			
	

			<form action='/login' method="post" accept-charset="utf-8" autocomplete="off" role="form" class="form-horizontal">
				<div class="form-group">
					<label for="name-input">
						User Name or Email
					</label>
					<input class="form-control" type="text" name="username" id="name-input" />
				</div>
				<div class="form-group">
					<label for="password-input">
						Password
					</label>
					<input class="form-control" type="password" name="password" id="password-input" />
				</div>
				<div class="row pt-3">
					<div class="col-md-6">
			
					</div>
					<div class="col-md-6">
						<button type="submit" id="submit" tabindex="5" class="btn btn-md btn-primary btn-outlined float-right">
							Submit
						</button>
					</div>
				</div>
			</form>
			<!-- Debug account: {0}:{1} -->
		</div>
	</div>
</div>

	</main>

	<footer class="footer">
		<div class="container text-center">
			<a href="https://ctfd.io">
				<small class="text-muted">Powered by CTFd</small>
			</a>
		</div>
	</footer>

	<script src="/themes/core/static/js/vendor/jquery.min.js"></script>
	<script src="/themes/core/static/js/vendor/markdown-it.min.js"></script>
	<script src="/themes/core/static/js/vendor/bootstrap.bundle.min.js"></script>
	<script src="/themes/core/static/js/style.js"></script>
	<script src="/themes/core/static/js/utils.js"></script>
	<script src="/themes/core/static/js/ezq.js"></script>
	<script src="/themes/core/static/js/events.js"></script>
	


	
</body>
</html>
'''.format(USERNAME, PASSWORD)
	return a
def htmlhello():
	return '''
	    <!DOCTYPE html>
<html>
<head>
	<title>UnderGroundCityCTF</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="shortcut icon" href="/themes/core/static/img/favicon.ico"
		  type="image/x-icon">
	<link rel="stylesheet" href="/themes/core/static/css/vendor/bootstrap.min.css">
	<link rel="stylesheet" href="/themes/core/static/css/vendor/font-awesome/fontawesome-fonts.css" type='text/css'>
	<link rel="stylesheet" href="/themes/core/static/css/vendor/font-awesome/fontawesome-all.min.css" type='text/css'>
	<link href='/themes/core/static/css/vendor/font.css' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" href="/themes/core/static/css/jumbotron.css">
	<link rel="stylesheet" href="/themes/core/static/css/sticky-footer.css">
	<link rel="stylesheet" href="/themes/core/static/css/base.css">
	
	
	<link rel="stylesheet" type="text/css" href="/static/user.css">
	<script src="/themes/core/static/js/vendor/promise-polyfill.min.js"></script>
	<script src="/themes/core/static/js/vendor/fetch.min.js"></script>
	<script src="/themes/core/static/js/CTFd.js"></script>
	<script src="/themes/core/static/js/vendor/moment.min.js"></script>
	<script src="/themes/core/static/js/vendor/nunjucks.min.js"></script>
	<script type="text/javascript">
		var script_root = "";
		var csrf_nonce = "4e233fb002887454a72a7cdb534a9e77c22942b6d2c5dd4752c699e408abafdd";
		var user_mode = "teams";
		CTFd.urlRoot = script_root;
	</script>
</head>
<body>
	<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
		<div class="container">
			<a href="/" class="navbar-brand">
				
				UnderGroundCityCTF
				
			</a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#base-navbars"
					aria-controls="base-navbars" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="base-navbars">
				<ul class="navbar-nav mr-auto">
					

					<li class="nav-item">
						<a class="nav-link" href="/notifications">Notifications</a>
					</li>
					
						<li class="nav-item">
							<a class="nav-link" href="/users">Users</a>
						</li>
						
						<li class="nav-item">
							<a class="nav-link" href="/teams">Teams</a>
						</li>
						
					
					
						<li class="nav-item">
							<a class="nav-link" href="/scoreboard">Scoreboard</a>
						</li>
					
					<li class="nav-item">
						<a class="nav-link" href="/challenges">Challenges</a>
					</li>
				</ul>

				<hr class="d-sm-flex d-md-flex d-lg-none">

				<ul class="navbar-nav ml-md-auto d-block d-sm-flex d-md-flex">
					
						
						<li class="nav-item">
							<a class="nav-link" href="/login">Login</a>
						</li>
					
				</ul>
			</div>
		</div>
	</nav>

	<main role="main">
		
	<div class="container">
	<div class="row">
    <div class="col-md-0 offset-md-1">
        <img class="w-100 mx-auto d-block" style="max-width: 1000px;padding: 50px;padding-top: 14vh;" src="http://image.xmsec.cc/udg1.jpg" />
        <h3 class="text-center">
            <p>参与挑战赛，赢得进入地下城的资格</p>

        </h3>
        <br>

    </div>
</div>
	</div>

	</main>

	<footer class="footer">
		<div class="container text-center">
			<a href="https://ctfd.io">
				<small class="text-muted">Powered by CTFd</small>
			</a>
		</div>
	</footer>

	<script src="/themes/core/static/js/vendor/jquery.min.js"></script>
	<script src="/themes/core/static/js/vendor/markdown-it.min.js"></script>
	<script src="/themes/core/static/js/vendor/bootstrap.bundle.min.js"></script>
	<script src="/themes/core/static/js/style.js"></script>
	<script src="/themes/core/static/js/utils.js"></script>
	<script src="/themes/core/static/js/ezq.js"></script>
	<script src="/themes/core/static/js/events.js"></script>
	
	

	
</body>
</html>
	'''
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)