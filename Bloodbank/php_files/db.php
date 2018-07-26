 <?php
// $conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");

// if ($conn->connect_error) {
// 	$a = array('errorCode' =>"1",'errorMsg'=>"$conn->connect_error");
// 	echo die(json_encode($a));
// }
 

 class Database{
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
			$this->myconn = $conn;

		}
		return $this->myconn;
 	}
 	function close(){
 		mysqli_close($CONN);
 	}

 }
?>