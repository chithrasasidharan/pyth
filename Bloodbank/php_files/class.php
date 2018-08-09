<?php 
include 'db.php';
$dbObj = new Database();
class Blood{

	function create($dbObj){
		$sql = "INSERT INTO `user` (Name,Username,Age,Gender,BloodGroup,District,State,PhoneNumber, Donor) VALUES ('{$_POST['Name']}','{$_POST['Username']}', '{$_POST['Age']}','{$_POST['Gender']}','{$_POST['BloodGroup']}','{$_POST['District']}','{$_POST['State']}','{$_POST['PhoneNumber']}','{$_POST['Donor']}');";
    		$res = $dbObj->executeQuery($sql);
			$id  = $dbObj->returnID();
			echo json_encode($id) ;
	}

	function delete($dbObj){
		$sql = "DELETE FROM `user` WHERE uid = '{$_GET['uid']}'";
		$res = $dbObj->executeQuery($sql);
		echo json_encode($res);
	}

	function update($dbObj){
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
		echo json_encode($res) ;
	}

	function search($dbObj){
		$sql = "SELECT uid,Name FROM user WHERE BloodGroup='{$_GET['BloodGroup']}';";
		$res = $dbObj->executeQuery($sql);
		$rows = array();
		if ($res->num_rows > 0) {
		    while($row = mysqli_fetch_row($res)){
		       $rows[] =  $row;
		    }
		    echo json_encode($rows);
		}
		else {
		    $a = array('errorCode' =>"2",'errorMsg'=>"No matching recd");
		    echo (json_encode($a));
		}
	}

	function retrieve($dbObj){
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
	}

	function login($dbObj){
		// session_start();
		if (isset($_POST['Username']) and isset($_POST['Password'])){
			$sql = "SELECT * FROM `user` WHERE Username='{$_POST['Username']}' and Password='{$_POST['Password']}'";
			$res = $dbObj->executeQuery($sql);
			// $data=mysql_num_rows($res);
			if($res->num_rows>0){
				$row = $res->fetch_assoc();
				echo json_encode($row);
				$res->free;
				echo (json_encode($res->num_rows));
				// 	// echo "Username or Password is wrong...!!!!";
			}
			else {
		    $a = array('errorCode' =>"2",'errorMsg'=>"No matching recd");
		    echo (json_encode($a));
			}
			return $res->num_rows;
		}
	}

}
?>