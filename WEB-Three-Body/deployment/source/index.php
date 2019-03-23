<?php

session_start();

if(isset($_POST['rand2']) && isset($_SESSION['rand2'])){
	if($_SESSION['rand2'] == $_POST['rand2']){
		$_SESSION['check'] = 1;	
		header("Location: /message.php");
		//to refresh the rand2, should not exit here 
		//exit();
	}else{
		alert('your answer is incorrect');	
		exit();
	}
}

$seed = rand();
srand($seed);
$rand1 = rand();
$rand2 = rand();
//echo $seed."\n";
//echo $rand1."\n";
//echo $rand2."\n";
$_SESSION['rand2'] = $rand2;

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
            <a class="nav-link active" href="#">Home</a>
            <a class="nav-link" href="/flag.php">Flag</a>
          </nav>
        </div>
      </header>

      <main role="main" class="inner cover">
        <h1 class="cover-heading">Solve the TB problem firstly</h1>
        <p class="lead">In centuries, the scientist in TB haven't solved this problem yet</p>
        <p class="lead">
	 	<div class="">
          		
          			<form class="" method='post' target='#' novalidate>
            				<div class="row">

              				<div class="col-md-4 mb-3">
                			<label for="firstName">body 1</label>
                			<input type="text" class="form-control" id="seed" placeholder="" value="<?php echo $seed;?>" disabled>
              				</div>

              				<div class="col-md-4 mb-3">
                			<label for="lastName">body 2</label>
                			<input type="text" class="form-control" id="rand1" placeholder="" value="<?php echo $rand1;?>" disabled>
					</div>

              				<div class="col-md-4 mb-3">
                			<label for="lastName">body 3</label>
                			<input type="text" name='rand2' class="form-control" id="rand2" placeholder="" value="" required>
					</div>

					</div>

					 <button class="btn btn-primary btn-lg btn-block" type="submit">Continue to checkout</button>
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
