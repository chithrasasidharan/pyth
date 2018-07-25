<?php
$conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");
 
if ($conn->connect_error) {
    $a = array('errorCode' =>"1",'errorMsg'=>"$conn->connect_error");
    echo die(json_encode($a));
}
$sql = "INSERT INTO `user` (Name,Age,Gender,BloodGroup,District,State,PhoneNumber, Donor)

VALUES
('{$_POST['Name']}','{$_POST['Age']}',
    '{$_POST['Gender']}','{$_POST['BloodGroup']}',
    '{$_POST['District']}','{$_POST['State']}','{$_POST['PhoneNumber']}','{$_POST['Donor']}');";

 if ($res =  mysqli_query($conn,$sql)) {
  echo "Query executed successfuly" ;
}
else {
   $a = array('errorCode' =>"3",'errorMsg'=>"ERROR: Could not able to execute $sql.".$mysqli->error);
        echo (json_encode($a));
}
$mysqli->close();
?>