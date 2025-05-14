<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>ProjectHub</title>
    <style type="text/css">
    	body {
  background-image: url('blur.jpg');
    background-size: cover;
}
    </style>
</head>
<body>

<?php
$sever ="localhost";
$username ="root";
$password ="";
$dbname ="project_hub";

//connection create.
$con = mysqli_connect("localhost", "root","","project_hub");

//connection check.
if(!$con)
{
	die("not connected: ".mysqli_connect_error());
}
error_reporting(E_ERROR | E_PARSE);
//insert data.
$C = $_POST['C'];
$C_PLUS =$_POST['C_PLUS'];
$HTML =$_POST["HTML"];
$JS = $_POST["JS"];
$JAVA = $_POST["JAVA"];
$Python = $_POST["Python"];
$PHP = $_POST["PHP"];
$RDBMS = $_POST["RDBMS"];


//insert into table.
$sql = "INSERT INTO categories(C, C_PLUS, HTML, JS, JAVA, Python, PHP, RDBMS) VALUES ('$C','$C_PLUS','$HTML','$JS','$JAVA','$Python','$PHP','$RDBMS')";

//Final Result.
$result = mysqli_query($con, $sql);
if ($result)
{
	echo "<center><h2>Project Language Submited Successfully.</h2></center>";

}
else
{
	echo "<h3>Account failed To Create</h3><br>".mysqli_error($con);
}

?>
</body>
<center><h3><button class="btn"><a href='home.html'>CONTINUE</a></button></h3><center>
	<br>
	<br>
	<br>
	<br>