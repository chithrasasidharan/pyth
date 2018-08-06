<?php
include 'class.php';
$b = new Blood();
$dbObj->connect();
$b->create($dbObj);
$dbObj->close();
?>
