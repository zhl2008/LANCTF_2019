<?php	
	try{
		if(isset($_GET['id'])&&isset($_GET['type']))
		{
			$id=htmlentities($_GET['id']);
			$type=htmlentities($_GET['type']);
			$id=str_replace("/","",$id);
			$type=str_replace("/","",$type);
			$filename="uploads/".str_replace(".","",$id).".".str_replace(".","",$type);
		}
		if(!file_exists($filename)){
			echo "图片不存在！";
		}
		else
			echo "<img src=\"".$filename."\"/>";
	}
	catch(Exception $e)
	{
		echo "ERROR";
	}
?>