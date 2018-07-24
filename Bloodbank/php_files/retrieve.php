<?php
$conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");
 
if ($conn->connect_error) {
    die("ERROR: Could not connect. "
                          .$conn->connect_error);
}
$sql = "SELECT * FROM user WHERE uid='{$_GET['uid']}';";
 if ($res =  mysqli_query($conn,$sql)) {
    if ($res->num_rows > 0) {
        while ($row = $res->fetch_array()) 
        {
            
          $ans = array( $row['uid'],$row['Name'],$row['Age'],
          	$row['Gender'], $row['BloodGroup'],$row['District'],
          	  $row['State'], $row['PhoneNumber'], $row['Donor'] ) ;
          $json = json_encode($ans);
          echo $json;
       
        }
        $res->free();
    }
    else {
        echo "No matching records are found.";
    }
}
else {
    echo "ERROR: Could not able to execute $sql. "
                                             .$mysqli->error;
}
$mysqli->close();
?>