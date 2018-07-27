<?php
include 'class.php';
$b = new Blood();
$dbObj->connect();
$b->create($dbObj);
$dbObj->close();
?>
<!-- // include 'db.php';

// $dbObj= new Database();
// $sql = "INSERT INTO `user` (Name,Age,Gender,BloodGroup,District,State,PhoneNumber, Donor)

// VALUES
// ('{$_POST['Name']}','{$_POST['Age']}',
//     '{$_POST['Gender']}','{$_POST['BloodGroup']}',
//     '{$_POST['District']}','{$_POST['State']}','{$_POST['PhoneNumber']}','{$_POST['Donor']}');";

// $res =  $dbObj->executeQuery($sql);
// $id  = $dbObj->returnID();
// echo json_encode($id) ; -->