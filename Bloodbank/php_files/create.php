<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "INSERT INTO `user` (Name,Age,Gender,BloodGroup,District,State,PhoneNumber, Donor)

VALUES
('{$_POST['Name']}','{$_POST['Age']}',
    '{$_POST['Gender']}','{$_POST['BloodGroup']}',
    '{$_POST['District']}','{$_POST['State']}','{$_POST['PhoneNumber']}','{$_POST['Donor']}');";

 if ($res =  mysqli_query($dbObj->myconn,$sql)) {
  echo "Query executed successfuly" ;
}
else {
   $a = array('errorCode' =>"3",'errorMsg'=>"ERROR: Could not able to execute $sql.".$mysqli->error);
        echo (json_encode($a));
}
$mysqli->close();
?>