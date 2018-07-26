
<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "SELECT uid,Name FROM user WHERE BloodGroup='{$_GET['BloodGroup']}';";
$dbObj->executeQuery($sql);
$dbObj->close();
?>