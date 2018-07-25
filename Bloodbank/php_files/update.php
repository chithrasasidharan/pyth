<?php
$conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");
 
if ($conn->connect_error) {
    $a = array('errorCode' =>"1",'errorMsg'=>"$conn->connect_error");
	echo die(json_encode($a));
}
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



if ($res =  mysqli_query($conn,$sql)) {
  echo "Query executed successfuly" ;
}
else {
    $a = array('errorCode' =>"3",'errorMsg'=>"ERROR: Could not able to execute $sql.".$mysqli->error);
		echo (json_encode($a));
}
$mysqli->close();
?>