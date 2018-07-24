<?php
$conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");
 
if ($conn->connect_error) {
    die("ERROR: Could not connect. "
                          .$conn->connect_error);
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
    echo "ERROR: Could not able to execute $sql. "
                                             .$mysqli->error;
}
$mysqli->close();
?>