
<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "SELECT uid,Name FROM user WHERE BloodGroup='{$_GET['BloodGroup']}';";
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
?>