<?php
include 'class.php';
$b = new Blood();
$dbObj->connect();
$b->delete($dbObj);
$dbObj->close();
?>
<!-- <?php
// include 'db.php';
// $dbObj= new Database();
// $dbObj->connect();

// $sql = "DELETE FROM `user` WHERE uid = '{$_GET['uid']}'";

// $res =  $dbObj->executeQuery($sql);
// echo json_encode($res);
// $mysqli->close();
?> -->