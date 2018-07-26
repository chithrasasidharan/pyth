<?php
include 'db.php';
$dbObj= new Database();
$dbObj->connect();
$a = array('Name' => $_POST['Name'] ,'Age'=>$_POST['Age'],'Gender'=>$_POST['Gender'], 'BloodGroup'=>$_POST['BloodGroup'],'District'=>$_POST['District'],'State'=>$_POST['State'],'PhoneNumber'=>$_POST['PhoneNumber'],'Donor'=>$_POST['Donor']);
$sql = "UPDATE user SET";
$comma = " ";
foreach ($a as $key => $value) {
	if(!empty($value)){
		$sql = $sql. $comma. " $key ='".$value ."' ";
		$comma = ",";
	}
}

$sql = $sql. "WHERE uid ='".$_GET['uid']."' ";



$res =  $dbObj->executeQuery($sql);
echo "Query executed successfuly" ;

$mysqli->close();
?>