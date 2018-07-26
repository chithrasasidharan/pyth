<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();

$sql = "INSERT INTO `user` (Name,Age,Gender,BloodGroup,District,State,PhoneNumber, Donor)

VALUES
('{$_POST['Name']}','{$_POST['Age']}',
    '{$_POST['Gender']}','{$_POST['BloodGroup']}',
    '{$_POST['District']}','{$_POST['State']}','{$_POST['PhoneNumber']}','{$_POST['Donor']}');";

$res =  $dbObj->executeQuery($sql);
$id  = $dbObj->myconn->insert_id;
echo json_encode($id) ;
$mysqli->close();
?>