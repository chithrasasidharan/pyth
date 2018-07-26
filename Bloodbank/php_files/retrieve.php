
<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "SELECT * FROM user WHERE uid='{$_GET['uid']}';";
$dbObj->executeQuery($sql);
$obj->close();
?>