
<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "SELECT uid,Name FROM user WHERE BloodGroup='{$_GET['BloodGroup']}';";
if ($res =  mysqli_query($dbObj->myconn,$sql)) {
    if ($res->num_rows > 0) {
    	$row = $res->fetch_assoc();
        echo json_encode($row);
        $res->free();
    }
    else {
    	$a = array('errorCode' =>"2",'errorMsg'=>"No matching recd");
		echo (json_encode($a));
    }
	// $rows = array();
    // while($r =  $res->fetch_assoc()){
    	// $rows[] = $r;
    // }
    // echo json_encode($rows);
}
else {
	$a = array('errorCode' =>"3",'errorMsg'=>"ERROR: Could not able to execute $sql.".$mysqli->error);
		echo (json_encode($a));
                                             // .$mysqli->error;
}
$mysqli->close();
?>