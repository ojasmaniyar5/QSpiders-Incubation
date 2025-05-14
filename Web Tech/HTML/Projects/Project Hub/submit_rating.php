<!-- submit_rating.php -->
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $rating = $_POST["rating"];

    // File to store ratings
    $ratingsFile = 'ratings.txt';

    // Append the new rating to the file
    file_put_contents($ratingsFile, $rating . PHP_EOL, FILE_APPEND);

    // Redirect to another page (display.php in this case)
    header("Location: display.php");
    exit();
}
?>
