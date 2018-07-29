<?php
	include 'class.php';
	$b = new Blood();
	$dbObj->connect();
	$b->search($dbObj);
	$dbObj->close();
?> 
<!-- <?php
// include 'db.php';
// $dbObj= new Database();
// $dbObj->connect();

// $sql ="SELECT uid,Name FROM `user` WHERE BloodGroup='{$_GET['BloodGroup']}';";
// $encsql = rawurlencode($sql);
// $res = $dbObj->executeQuery($sql);
// if ($res->num_rows > 0) {
//     while($row = mysqli_fetch_assoc($res)){
//     	echo json_encode($row);
//     }
    
// }
// else {
//     $a = array('errorCode' =>"2",'errorMsg'=>"No matching recd".$sql);
//     echo (json_encode($a));
// }
// $dbObj->close();
?>  -->