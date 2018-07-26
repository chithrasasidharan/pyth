<?php
class Database{

	function ConnectDB(){
		$conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");

		if ($conn->connect_error) {
			$a = array('errorCode' =>"1",'errorMsg'=>"$conn->connect_error");
			echo die(json_encode($a));
		}
	}
		
}
$db = new Database;
?>
 
