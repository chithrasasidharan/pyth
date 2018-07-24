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
            
            echo json_encode($row['uid'])   ;
            echo json_encode($row['Name']) ;
            echo json_encode($row['Age'] );
            echo json_encode($row['Gender'] );
            echo json_encode($row['BloodGroup'] );
            echo json_encode($row['District'] );
            echo json_encode($row['State'] );
            echo json_encode($row['PhoneNumber'] );
            echo json_encode($row['Donor']);
           
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