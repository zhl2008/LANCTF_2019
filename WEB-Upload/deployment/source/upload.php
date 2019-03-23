<?php  
include 'function.php';
if(isset($_POST['submit']) && !empty($_FILES['image']['tmp_name']))
{	
	$name = $_FILES['image']['tmp_name'];
	$type = $_FILES['image']['type'];
	$size = $_FILES['image']['size'];

	if(!is_uploaded_file($name))
	{
		?>
		<div class="alert alert-danger" role="alert">上传失败,请重新上传</div>
		<?php
			exit;
	}	


	if($size > 10240)
	{
		?>
		<div class="alert alert-danger" role="alert">大小超过10KB</div>
		<?php
			exit;	
	}

	$imagekey = create_imagekey();
	move_uploaded_file($name,"uploads/$imagekey.php");

	echo "<script>window.location.href='uploads/$imagekey.php';</script>";
}
?>
