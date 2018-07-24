<?php
$conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");
 
if ($conn->connect_error) {
    die("ERROR: Could not connect. "
                          .$conn->connect_error);
}
$sql = "DELETE FROM `user` WHERE uid = '{$_GET['uid']}'";

 if ($res =  mysqli_query($conn,$sql)) {
  echo "Query executed successfuly" ;
}
else {
    echo "ERROR: Could not able to execute $sql. "
                                             .$mysqli->error;
}
$mysqli->close();
?>