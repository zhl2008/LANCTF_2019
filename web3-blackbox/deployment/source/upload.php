<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
<?php
$error=$_FILES['pic']['error'];
$tmpName=$_FILES['pic']['tmp_name'];
$name=$_FILES['pic']['name'];
$size=$_FILES['pic']['size'];
$type=$_FILES['pic']['type'];
try{
	if($name!=="")
	{
		$name1=substr($name,-4);
		if(is_uploaded_file($tmpName)){
			$time=time();
			$rootpath='uploads/'.$time.$name1;
			if(!move_uploaded_file($tmpName,$rootpath)){
				echo "<script language='JavaScript'>alert('文件移动失败!');window.location='index.php?page=submit'</script>";
				exit;
			}
			else{
				if($type!=="image/jpeg"&&$type!=="image/gif")
				{
					echo $type;
					echo "<script language=javascript>alert('不允许的文件类型!upload jpg or gif');history.go(-1)</script>";
					unlink($rootpath);
					exit;
				}
				if($name1===".php"){
					file_put_contents($rootpath,preg_replace("/\?/","",file_get_contents($rootpath)));
				}
				
			}
		}
		echo "图片ID：".$time;
	}
}
catch(Exception $e)
{
	echo "ERROR";
}
//
 ?>
 </html>
