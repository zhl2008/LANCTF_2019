<?php
	require("header.php");
	include_once("config/config.php");
	if(!isset($_COOKIE['authe'])){
		//secret_is_'hash.??????'
		$autharr=array(
			'role'=>'guest',
			'passnum'=>'????????'
			);
		$auth= json_encode($autharr);
		ob_start();
		setcookie('authe', $auth);
		ob_end_clean();
		$_SESSION['isguest']=true;
	  }else{
		$temp=$_COOKIE['authe'];
		$data=json_decode($temp);
		$num=$data->passnum;
		if(json_last_error() != JSON_ERROR_NONE){
			echo "json error";
			exit();
		}
		if($num!=="????????"){
			for ($i=0; $i < 8; $i++) { 
				//secret num is random generated that you can't guess, only admin can enter this site.
				if(!($num[$i]==$secretnum[$i]))
				{
					echo "random secret num error";
					exit();
				}
				
			}
			if($data->role==='admin'){
				$_SESSION['isguest']=false;
			}
		}

	  }
	$page="";
	if (isset($_GET['page']))
	{
		$page=strtolower($_GET['page']);
		$page=str_replace("#", "", $page);
		$page=str_replace("'", "", $page);
		if(strpos($page,"config")!==false)
			exit();
		if(strpos($page,"phar")!==false||strpos($page,"zip")!==false||strpos($page,"data")!==false)
			exit();
		
		$page=$_GET['page'].".php";
	}
	else
		$page="main.php";

	
	if(!isset($_SESSION['isguest'])||$_SESSION['isguest']===true)
	{
		echo "游客(guest)不允许访问更多功能";
		exit();
	}	
	include($page);
?>