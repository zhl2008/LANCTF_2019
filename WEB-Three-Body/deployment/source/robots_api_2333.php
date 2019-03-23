<?php
/*
if(!($_SERVER['REMOTE_ADDR'] == '127.0.0.1')){
    exit('fuck off!');
}
*/
header("Access-Control-Allow-Origin: *");
//connect
$conn = mysql_connect("localhost:3306","root","");
if (!$conn){
    die('Could not connect: ' . mysql_error());
}
mysql_select_db("haozi",$conn);

//get one record
$sql = "select * from msg order by id limit 0,1";
$res = mysql_query($sql,$conn);

while($row = mysql_fetch_array($res)){

    echo $row['id'] . ":" . base64_decode($row['contents']) . "\n" ;
    //delete finished record
    $sql = "delete from msg where id=".$row['id'];
    mysql_query($sql,$conn);

}

echo "Done!\n";

mysql_close($conn);


