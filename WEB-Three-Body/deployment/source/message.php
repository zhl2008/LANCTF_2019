<?php

session_start();
if(!$_SESSION['check']){
    alert('please solve the TB problem firstly!');   
}


if(isset($_POST['msg'])){
    $conn = mysql_connect("localhost:3306","root","");

    if (!$conn){
	die('Could not connect: ' . mysql_error());
    }

    mysql_select_db("haozi",$conn);
    $content = base64_encode($_POST['msg']);
    $sql = "INSERT INTO msg (contents) VALUES ('".$content."')";
    mysql_query($sql,$conn);

    //re-solve the TB problem to avoid bruteforce
    $_SESSION['check'] = 0;

    echo '<script>alert("success!");window.location.href="/index.php";</script>';

    exit();
}

function alert($msg){
	echo '<script>alert("'.$msg.'");history.go(-1);</script>';
}

?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Cover Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="cover.css" rel="stylesheet">
  </head>

  <body class="text-center">

    <div class="cover-container d-flex h-100 p-3 mx-auto flex-column">
      <header class="masthead mb-auto">
        <div class="inner">
          <h3 class="masthead-brand">Cover</h3>
          <nav class="nav nav-masthead justify-content-center">
            <a class="nav-link active" href="#">Message</a>
            <a class="nav-link" href="/flag.php">Flag</a>
          </nav>
        </div>
      </header>

      <main role="main" class="inner cover">
        <h1 class="cover-heading">Gravitational Wave Signal System</h1>
        <p class="lead">Broadcast our position to the whole universe via Gravitational Wave to communicate with the high-level lives</p>
        <p class="lead">
	 	<div class="">
		    <form class="card p-2" method="post" target="#">
			<div class="input-group">
			    <input type="text" name='msg' class="form-control" placeholder="hello alien!">
			    <div class="input-group-append">
				<button type="submit" class="btn btn-secondary">Send</button>
			    </div>
			</div>
		    </form>	
            	</div>
      </p>
      </main>

      <footer class="mastfoot mt-auto">
        <div class="inner">
          <p>Cover template for <a href="https://getbootstrap.com/">Bootstrap</a>, by <a href="https://twitter.com/mdo">@mdo</a>.</p>
        </div>
      </footer>
    </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="js/jquery-slim.min.js"><\/script>')</script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
