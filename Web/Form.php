<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $DVQL = $_POST["DVQL"];
    $Tuyen = $_POST["tuyen"];
    $BKS = $_POST["BKS"];

    $file = fopen("BusInfor.txt" , "a");
    fwrite($file, $DVQL. '/' . $Tuyen . '/' . $BKS. PHP_EOL);
    //fwrite($file, "\n";
    fclose( $file );

    // Redirect to index.php and pass data as URL parameters
    header("Location: http://localhost:3000/Web/index.php");
    exit();
}
?>