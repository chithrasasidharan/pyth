<?php
include 'db.php';
$sql = "DELETE FROM `user` WHERE uid = '{$_GET['uid']}'";

 if ($res =  mysqli_query($conn,$sql)) {
  echo "Query executed successfuly" ;
}
else {
    $a = array('errorCode' =>"3",'errorMsg'=>"ERROR: Could not able to execute $sql.".$mysqli->error);
		echo (json_encode($a));
}
$mysqli->close();
?>