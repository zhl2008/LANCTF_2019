<?php  
error_reporting(0);

@session_start();
//posix_setuid(1000);

$fp = empty($_GET['fp']) ? 'fail' : $_GET['fp'];
if(preg_match('/\.\./',$fp))
{
	die('No No No!');
}
if(preg_match('/rm/i',$_SERVER["QUERY_STRING"]))
{
	die();
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title></title>
		<meta charset="utf-8">
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<link href="css/jumbotron-narrow.css" rel="stylesheet">
	</head>
	<body>
		<div class="container">
			<div class="header clearfix">
				<nav>
					<ul class="nav nav-pills pull-right">
						<li role="presentation" class="active"><a href="home.php?key=haozigege">Home</a></li>
					</ul>
				</nav>
				<h3 class="text-muted">Fuel Upload</h3>
			</div>

			<div class="jumbotron">
				<h1>Fuel Upload</h1>
				<p class="lead">Upload your fuel but u must be quickly</p>
				<form action="?fp=upload" method="POST" id="form" enctype="multipart/form-data">
					<input type="file" id="image" name="image" class="btn btn-lg btn-success" style="margin-left: auto; margin-right: auto;">
					<br>
					<input type="submit" id="submit" name="submit" class="btn btn-lg btn-success" role="button" value="Upload">
				</form>
			</div>
	   	</div> 
	</body>
</html>
<?php  
if($fp !== 'fail')
{
	if(!(include($fp.'.php')))
	{
		?>
		<div class="alert alert-danger" role="alert">没有此页面</div>
		<?php
			exit;
	}
}
?>
