<?php
function adder($x,$y){
	echo $x+$y;
}
adder($_GET["x"],$_GET["y"]);
?>