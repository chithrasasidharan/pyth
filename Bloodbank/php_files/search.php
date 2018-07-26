
<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "SELECT uid,Name FROM user WHERE BloodGroup='{$_GET['BloodGroup']}';";
$res = $dbObj->executeQuery($sql);
$rows = array();
if ($res->num_rows > 0) {
    while($row = mysqli_fetch_row($res)){
       $rows[] =  $row;
    }
    $res->free();
    echo json_encode($rows);
}
else {
    $a = array('errorCode' =>"2",'errorMsg'=>"No matching recd");
    echo (json_encode($a));
}
$dbObj->close();
?>