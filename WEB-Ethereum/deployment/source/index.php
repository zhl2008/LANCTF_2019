<?php

//if (isset($_GET['source'])) {
//    die(highlight_file(__FILE__));
//}

require("config.php");
error_reporting(0);

session_start();
if (isset($_POST['secret'])) {
    $query = $conn->prepare("INSERT INTO secrets(session_id, secret) VALUES (?, ?)");
    $current_session_id = session_id();
    $query->bind_param('ss', $current_session_id, $_POST['secret']);
    $query->execute();
    
}
if(isset($_COOKIE['PHPSESSID'])) {
    $query = "SELECT * FROM secrets WHERE session_id = '" .$_COOKIE['PHPSESSID'] . "'";
    $result = $conn->query($query);
}

?>

<!DOCTYPE HTML>
<meta charset="UTF-8">
<html>
<head>
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    </head>
    <body>
        <div id="custom-bootstrap-menu" class="navbar navbar-default " role="navigation">
            <div class="container-fluid">
            <div class="navbar-header"><a class="navbar-brand" href="#">Ethererum私钥存储系统</a>
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-menubuilder"><span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span>
                </button>
            </div>
            <div class="collapse navbar-collapse navbar-menubuilder">
                <ul class="nav navbar-nav navbar-left">
                <li><a href="#">Home</a>
                </li>
                </ul>
            </div>
            </div>
        </div>
        <div class="container-fluid">
	<?php
	if (isset($_POST['secret'])) {
	    echo '<div class="alert alert-success" role="alert">Ethereum私钥添加成功，你的token是: '. session_id() .'</div>';
	}
	?>
	<div class="row">
	    <div class="col-md-2"></div>
	    <div class="col-md-8">
		<form method="POST" action="/index.php">

		    <div class="input-group">
		      <input type="text" name="secret" class="form-control" placeholder="Your private key" aria-describedby="basic-addon2">
		      <span class="input-group-btn">
			<button class="btn btn-default" type="submit">添加</button>
		     </span>
		    </div>
		</form>
	    </div>
	    <div class="col-md-2"></div>
	</div>
    </div>

    <br/>
    <br/>
    <br/>

        <div class="container-fluid">
	<div class="row">
	    <div class="col-md-4"></div>
	    <div class="col-md-4">
		<div class="panel panel-default">
		  <div class="panel-heading">你的私钥</div>

		  <!-- Table -->
		  <table class="table">
		    <?php
		    if (isset($result) && $result->num_rows > 0) {
		        // output data of each row
		        while($row = $result->fetch_assoc()) {
			echo "<tr><td>" . htmlspecialchars($row['secret']) . "</td></tr>";
		        }
		    } else {
			echo "<tr><td>You don't have any secrets yet.</td></tr>";
		    }
		    ?>
		  </table>
		</div>
	    </div>
	    <div class="col-md-4"></div>
	</div>

        </div>

    <script
              src="https://code.jquery.com/jquery-3.1.1.min.js"
              integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
              crossorigin="anonymous"></script>

        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


</body>
</html>
