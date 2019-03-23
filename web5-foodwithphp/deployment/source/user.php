<?php
require_once("function.php");
if( !isset( $_SESSION['user'] )){
    Header("Location: index.php");

}

//die($_SESSION['isadmin']);
if($_SESSION['isadmin'] === '1'){
    if(!isset($_GET['page']) || $_GET['page'] === ''){
        $page = 'info';
    }else {
        $page = $_GET['page'];
    }
}
else{
    if(!isset($_GET['page'])|| $_GET['page'] === ''){
        $page = 'guest';
    }else {
        $page = $_GET['page'];
        if($page === 'info') 
        {
//          echo("<script>alert('no premission to visit info, only admin, you are guest')</script>");
            Header("Location: user.php?page=guest");
        }
    }
}
filter_directory();

file_exists("$page")?include "$page":include "$page.php";
?>