<?php
include 'class.php';
$b = new Blood();
$dbObj->connect();
$b->retrieve($dbObj);
$dbObj->close();
?>
<!-- <?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "SELECT * FROM user WHERE uid='{$_GET['uid']}';";
$res = $dbObj->executeQuery($sql);

if ($res->num_rows > 0) {
    $row = $res->fetch_assoc();
    echo json_encode($row);
    $res->free();
}
else {
    $a = array('errorCode' =>"2",'errorMsg'=>"No matching recd");
    echo (json_encode($a));
}
$dbObj->close();
?> -->