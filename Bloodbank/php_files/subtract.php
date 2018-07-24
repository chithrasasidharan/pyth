<?php
function adder($x,$y){
	echo $x-$y;
}
adder($_POST["x"],$_POST["y"]);
?>