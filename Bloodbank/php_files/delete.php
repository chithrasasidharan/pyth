<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "DELETE FROM `user` WHERE uid = '{$_GET['uid']}'";

 if ($res =  mysqli_query($dbObj->myconn,$sql)) {
  echo "Query executed successfuly" ;
}
else {
    $a = array('errorCode' =>"3",'errorMsg'=>"ERROR: Could not able to execute $sql.".$mysqli->error);
		echo (json_encode($a));
}
$mysqli->close();
?>