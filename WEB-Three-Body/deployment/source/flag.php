<?php
$flag = "LANCTF{P1E4SE_H4ck_3V3RY_7H1NG}";
if($_SERVER['REMOTE_ADDR'] == '127.0.0.1'){

    echo $flag;

}else{
     
    echo 'fuck off!';
    echo $_SERVER['REMOTE_ADDR'];

}


