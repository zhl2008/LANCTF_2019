<?php
session_start();
rand(1,9);
rand(1,9);
$secretnum="";
for ($i=0; $i < 8; $i++) { 
    $secretnum=$secretnum.(string)rand(1,9);
}


?>