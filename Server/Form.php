<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $DVQL = $_POST["DVQL"];
    $Tuyen = $_POST["tuyen"];
    $BKS = $_POST["BKS"];

    // Redirect to index.php and pass data as URL parameters
    header("Location: http://localhost:3000/Server/index.php?DVQL=" . urlencode($DVQL) . "&tuyen=" . urlencode($Tuyen) . "&BKS=" . urlencode($BKS));
    exit();
}
?>