<?php
$conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");
 
if ($conn->connect_error) {
    $a = array('errorCode' =>"1",'errorMsg'=>"$conn->connect_error");
	echo die(json_encode($a));
}
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