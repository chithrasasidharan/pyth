$(document).ready(function(){
	$("#log").click(function(){
		var email = $("#uname").val();
		var password = $("#pwd").val();
// Checking for blank fields.
		if( email =='' || password ==''){
			$('input[type="text"],input[type="password"]').css("border","2px solid red");
			$('input[type="text"],input[type="password"]').css("box-shadow","0 0 3px red");
			alert("Please fill all fields...!!!!!!");
		}
		else {
			$.post("http://localhost:8080/php_files/login.php",{ Username: email, Password:password},
			function(data) {
				alert("here");
				console.log(data);
				if(data==0){
					$('input[type="text"],input[type="password"]').css({"border":"2px solid red","box-shadow":"0 0 3px red"});
					alert(data);
					window.location.href="/mnt/E23043AE3043890D/python/Bloodbank/html_files/front.html"
				}
				else if(data==1){
					$('input[type="text"],input[type="password"]').css({"border":"2px solid #00F5FF","box-shadow":"0 0 5px #00F5FF"});
					window.location.href="/mnt/E23043AE3043890D/python/Bloodbank/html_files/login.html"
				}
				else{
					alert(data);
				}
			});
		}
	});
});