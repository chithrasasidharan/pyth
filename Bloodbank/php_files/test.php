<?php
$conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");
 
if ($conn->connect_error) {
    die("ERROR: Could not connect. "
                          .$conn->connect_error);
}
$sql = "SELECT * FROM user";
  echo "Query executed successfuly" ;
if ($res =  mysqli_query($conn,$sql)) {
    if ($res->num_rows > 0) {
        echo "<table>";
        echo "<tr>";
        echo "<th>uid</th>";
        echo "<th>Name</th>";
        echo "<th>Age</th>";
        echo "<th>Gender</th>";
        echo "<th>bg</th>";
        echo "<th>Dist</th>";
        echo "<th>State</th>";
        echo "<th>Ph</th>";
        echo "<th>Donor</th>";
        echo "</tr>";
        while ($row = $res->fetch_array()) 
        {
            echo "<tr>";
            echo "<td>".$row['uid']."</td>";
            echo "<td>".$row['Name']."</td>";
            echo "<td>".$row['Age']."</td>";
            echo "<td>".$row['Gender']."</td>";
            echo "<td>".$row['BloodGroup']."</td>";
            echo "<td>".$row['District']."</td>";
            echo "<td>".$row['State']."</td>";
            echo "<td>".$row['PhoneNumber']."</td>";
            echo "<td>".$row['Donor']."</td>";
            echo "</tr>";
        }
        echo "</table>";
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