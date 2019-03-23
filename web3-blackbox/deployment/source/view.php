   
   <div class="container">
	  <form class="form-signin" action="show.php" method="GET">
			<h2 class="form-signin-heading">View</h2>
			<label for="PictureID" class="sr-only">PictureID</label>
			<input type="text" id="PictureID" name="id" class="form-control" placeholder="PictureID" required autofocus>
			<label for="PictureType" class="sr-only">PictureID</label>
			<input type="text" id="PictureType" name="type" class="form-control" placeholder="PictureType">
			<?php
				if(isset($_GET['id'])&&isset($_GET['type']))
				{
					$filename=$_GET['id'].$_GET['type'];
				}
			?>
			<button class="btn btn-lg btn-primary btn-block" type="submit">Submit</button>
		  </form>
		 </div>