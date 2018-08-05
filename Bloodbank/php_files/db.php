 <?php
// $conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");

// if ($conn->connect_error) {
// 	$a = array('errorCode' =>"1",'errorMsg'=>"$conn->connect_error");
// 	echo die(json_encode($a));
// }
 

 class Database{
	private $myconn;
 	function connect(){
		$user = "newuser";
		$pass = "cleartext_password";
		$server = "localhost";
		$db = "Bloodbank";
		$conn = new mysqli($server,$user,$pass,$db);
		if($conn->connect_error){
			$a = array('errorCode' =>"1",'errorMsg'=>"$conn->connect_error");
			echo die(json_encode($a));
		}
		else{
			echo "connected";
			$this->myconn = $conn;

		}
 	}
 	function close(){
 		mysqli_close($this->myconn);
 	}

 	function executeQuery($sql){
 		if ($res =  mysqli_query($this->myconn,$sql)) {
 			return $res;
		    
		}
		else {
			$a = array('errorCode' =>"3",'errorMsg'=>"ERROR: Could not execute $sql.".$mysqli->error);
				echo (json_encode($a));
		}
 	}
 	function returnID(){
 		return $this->myconn->insert_id;

 	}

 	

 }
?>