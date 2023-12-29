<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <?php
    $page = $_SERVER['PHP_SELF'];
    $sec = "5";
    ?>
    <!-- 
    <meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'">
    -->

    
    <title>Thông tin xe</title>

    <!-- Connect to database -->
    <?php
        include "ConnectDB.php";
    ?>

    <?php
        // Retrieve passed parameters from URL
        $DVQL = isset($_GET["DVQL"]) ? $_GET["DVQL"] : "N/A";
        $Tuyen = isset($_GET["tuyen"]) ? $_GET["tuyen"] : "N/A";
        $BKS = isset($_GET["BKS"]) ? $_GET["BKS"] : "N/A";
    ?>

    <!-- link css -->
    <link rel="stylesheet" href="style.css">

    <!-- SET LIVE TIME -->
    <script src="LiveTime.js"></script>

</head>

<body onload = display_ct7();>
    
    <h1>BUS INFORMATION</h1>
    
    <div class = "Button">  
        <ul><button><a href="ChangeBus.php">Thay đổi thông tin xe</a></button></ul>    
        <ul><button><a href="index.php">Refresh</a></button></ul>   
    </div>

    <table>
        <!--Thời gian thực  -->
        <tr style="background-color: gray;">
            <th colspan = "2" >Date - Time:  &emsp; <span id = 'ct7'></span></th>
        </tr>

        <!-- Đơn vị quản lý  -->
        <tr style="background-color: gray;">
            <?php
                echo "<th colspan= \"2 \">Đơn vị quản lý: ";
                echo $DVQL;
                echo "</th>";
            ?>
        </tr>

        <!-- Tuyến -->
        <tr style="background-color: gray;">
        <?php
                echo "<th colspan= \"2 \"> Tuyến : ";
                echo $Tuyen;
                echo "</th>";
            ?>
        </tr>

        <!-- Biển kiểm soát -->
        <tr style="background-color: gray;">
            <?php
                echo "<th colspan= \"2 \">Biển kiểm soát: ";
                echo $BKS;
                echo "</th>";
            ?>
        </tr>

        <!-- Số hành khách Vào/ Ra -->
        <?php
            include("GetPassenger.php")
        ?>
    </table>
</body>
</html>