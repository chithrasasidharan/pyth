<?php
$conn = new mysqli("localhost", "newuser", "cleartext_password", "Bloodbank");
 
if ($conn->connect_error) {
    die("ERROR: Could not connect. "
                          .$conn->connect_error);
}
public function update($data, $table, $where){
	$data_str = '';

	foreach ($data as $column=> $value) {
		if(!empty($data_str))
			$data_str.=',';
	}
	$sql = "UPDATE $table SET $data_str WHERE $where";
	mysqli_query($sql) or die(mysql_error());
	return true;
}
// $allowed = array('Name','PhoneNumber');
// $data = $db->filterArray($_POST,$allowed);
// $sql = "UPDATE user SET ?u uid = '{$_GET['uid']};";

// update('{$_POST['Name']}',user,uid='{$_GET['uid']}');
//  if ($res =  mysqli_query($conn,$sql)) {
//   echo "Query executed successfuly" ;
// }
// else {
//     echo "ERROR: Could not able to execute $sql. "
//                                              .$mysqli->error;
// }
$mysqli->close();
?>