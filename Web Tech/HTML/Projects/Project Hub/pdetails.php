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
$cname = $_POST['cname'];
$d_name =$_POST['sname'];
$s_desc =$_POST["dis"];
$s_sugge =$_POST["suggestion"];
$p_date = $_POST["pdate"];
$image = $_POST["image"];
$pdf = $_POST["pdf"];
$video = $_POST["video"];


//insert into table.
$sql = "INSERT INTO project_details(cname, d_name, s_desc, s_sugge, p_date, image, pdf, video) VALUES ('$cname','$d_name','$s_desc','$s_sugge','$p_date','$image','$pdf','$video')";

//Final Result.
$result = mysqli_query($con, $sql);
if ($result)
{
	echo "<center><h2>Details Submited Successfully.</h2></center>";

}
else
{
	echo "<h3>failed To Submit.</h3><br>".mysqli_error($con);
}

     
echo "<b>Student Name :</b>".$cname;
echo "<br>";
echo "<b>Developer Name :</b>".$d_name;
echo "<br>";
echo "<b>Description :</b>".$s_desc;
echo "<br>";
echo "<b>Suggestion :</b>".$s_sugge;
echo "<br>";
echo "<b>Date :</b>".$p_date;
echo "<br>";
echo "<b>Image :</b>".$image;
echo "<br>";
echo "<b>pdf :</b>".$pdf;
echo "<br>";
echo "<b>video:</b>".$video;




















?>
</body>
<center><h3><button class="btn"><a href='demo.html'>Back.</a></button></h3><center>
	<br>
	<br>
	<br>
	<br>