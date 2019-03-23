<?php
	require("header.php");
	$page="";
	if (isset($_GET['page']))
	{
		$page=strtolower($_GET['page']);
		$page=str_replace("#", "", $page);
		$page=str_replace("'", "", $page);
		if(strpos($_GET['page'],"://")!==false){
			echo "<script language=javascript>alert('No protocol！');history.go(-1)</script>";
			exit();
		}
		$page=$_GET['page'].".php";
	}
	else
		$page="main.php";
	include($page);
?>