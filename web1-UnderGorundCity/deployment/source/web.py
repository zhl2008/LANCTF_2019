# -*- coding:utf-8 -*-
import hashlib
import logging
import os
from datetime import timedelta

from flask import Flask
from flask import request
from flask import config
from flask import session
from flask import render_template_string


class Config(object):
    ACCOUNT = 'udgame'
    PASSWORD = 'udg'
class ProductionConfig(Config):
    HOST = '127.0.0.1'
    PORT = 65521
    DBUSERNAME = 'udgame'
    DBPASSWORD = 'udg'
    DBNAME = 'udg'

app = Flask(__name__,static_folder="themes")


app.config['secret'] = "LANCTF{c3c9bf81b15cf03206420fb2d0f3f636}"
app.config.from_object(ProductionConfig) 
app.permanent_session_lifetime = timedelta(hours=6) 
page_size = 60
app.config['UPLOAD_DIR'] = '/var/www/html/upload'
app.config['PLUGIN_UPDATE_URL'] = 'https://xmsec/update'
app.config['PLUGIN_DOWNLOAD_ADDRESS'] = 'https://xmsec/download'



@app.route('/')
def hello_world():
    tem='''
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
    return render_template_string(tem)

@app.errorhandler(404)
def page_not_found(e):
    uurl=request.url

    if ">" in request.url or "&" in request.url or "-" in request.url or "%26" in request.url or "%3e" in request.url.lower():
        return "FORBIDEN"
    if "os" in request.url or  "self" in request.url or "system" in request.url:
        return "I know what you did! But flag you want is in config."
    if "'current_app" in request.url:
        uurl= "LANCTF{ .... <br> 抄current_app也要懂ssti才对嘛，你的current_app好像被过滤了"
    
    template = '''
    {{% set config='flag is in config, but var config was clear'%}}
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
		<div class="col-md-12">
			<h1 class="text-center">404</h1>
			<h2 class="text-center">Whoops, looks like we can't find {url}.</h2>
			<h2 class="text-center">Sorry about that</h2>
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
    <!-- maybe ssti help u-->
	<script src="/themes/core/static/js/vendor/jquery.min.js"></script>
	<script src="/themes/core/static/js/vendor/markdown-it.min.js"></script>
	<script src="/themes/core/static/js/vendor/bootstrap.bundle.min.js"></script>
	<script src="/themes/core/static/js/style.js"></script>
	<script src="/themes/core/static/js/utils.js"></script>
	<script src="/themes/core/static/js/ezq.js"></script>
	<script src="/themes/core/static/js/events.js"></script>
	


	
</body>
</html>
    '''.format(url=uurl)
    return render_template_string(template), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)