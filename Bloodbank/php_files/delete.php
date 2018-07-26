<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "DELETE FROM `user` WHERE uid = '{$_GET['uid']}'";

$res =  $dbObj->executeQuery($sql);
echo json_encode($res);
$mysqli->close();
?>