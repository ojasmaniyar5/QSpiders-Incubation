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
$cname=$_POST['cname'];
$sname=$_POST['sname'];
$dis=$_POST['dis'];
$data=$_POST['date'];
$image=$_POST['image'];
$pdf=$_POST['pdf'];
$video=$_POST['video'];

echo "<br><br><u>College Name</u> : ".$cname;
echo "<br><br><u>Developers(Student)</u> : ".$sname;
echo "<br><br><u>Short Discription</u> : ".$dis;
echo "<br><br><u>Technology(Programming Language)</u> : ".$data;
echo "<br><br><u>Upload image</u> : ".$image;
echo "<br><br><u>Upload pdf</u> : ".$pdf;
echo "<br><br><u>Upload video</u> : ".$video;
?>
</body>