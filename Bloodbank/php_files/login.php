<?php
	include 'class.php';
	$b = new Blood();
	$dbObj->connect();
	$b->login($dbObj);
	// $dbObj->close();
?>