<?php
	include_once("config/config.php");
	if(!isset($_SESSION['isguest'])||$_SESSION['isguest']===true)
	{
		echo "游客(guest)不允许访问更多功能";
		exit();
	}	
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
			echo "图片不存在！注：图片命名方式已变更，旧版访问方式将在近期更新，服务暂不可用";
		}
		else
			echo "<img src=\"".$filename."\"/>";
	}
	catch(Exception $e)
	{
		echo "ERROR";
	}
?>