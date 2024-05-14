<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thông tin xe</title>

    <!-- Connect to database and Get current bus information -->
    <?php
        include "InitBuS.php";
    ?>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="AutoUpdateData.js"></script>

    <script src = "https://www.gstatic.com/firebasejs/8.2.9/firebase-app.js"></script>
    <script src = "https://www.gstatic.com/firebasejs/8.2.9/firebase-database.js"></script>
    <script src= "getDataFromDB.js"></script>

    <!-- get current url -->
    <?php  
        if(isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on')   
            $url = "https://";   
        else  
            $url = "http://";   
        // Append the host(domain name, ip) to the URL.   
        $url.= $_SERVER['HTTP_HOST'];   
        
        // Append the requested resource location to the URL   
        $url.= $_SERVER['REQUEST_URI'];    
  ?>   

    <!-- link css -->
    <link rel="stylesheet" href="style.css">

    <!-- SET LIVE TIME -->
    <script src="LiveTime.js"></script>

</head>

<body onload = display_ct7();>
    
    <h1>BUS INFORMATION</h1>
    <script>
        let currentURL = window.location.href;
    </script>

    <div class = "Button">  
        <ul><button><a href="ChangeBus.php">Thay đổi thông tin xe</a></button></ul>    
        <ul><button>
            <?php
                echo "<a href= \" ". $url ."\"  >Refresh</a>";
            ?>
        </button></ul>   
    </div>
    
    <table>
    <tr style="background-color: gray;">
        <th colspan = "2" > Date - Time :   <span id = 'ct7'></span></th>
    </tr>

    <!-- Đơn vị quản lý -->
    <tr style="background-color: gray;"><th colspan= "2">Đơn vị quản lý:
        <?php
            echo $DVQL;
        ?>
    </th></tr>

    <!-- Tuyến -->
    <tr style="background-color: gray;">
    <th colspan= "2 "> Tuyến :
        <?php
            echo $Tuyen;
        ?>
    </th></tr>

    <!-- Biển kiểm soát -->
    <tr style="background-color: gray;">
    <th colspan= "2 ">Biển kiểm soát:
        <?php
            echo $BKS;
        ?>
    </th></tr>

    <!-- Khách vào ra -->
    <tr >
    <th style="background-color: green;">Số khách vào</th>
    <th style="background-color: red;"> Số khách ra</th>
    </tr>

    <!-- Hiển thị  số khách vào ra -->
    <tr>
    <th id = "numberIn"></th>
    <th id = "numberOut"></th>
    </tr>

    <!--  Số hành khách hiện tại -->
    <tr>
    <th style="background-color: #ffcc00;" , colspan = "2">Số khách trên xe</th>
    </tr>  
    <th colspan = "2" id = "numberCur"></th>

    <!-- // Trạng thái Camera -->
    <tr style = "background-color: gray;">
    <th class="statusText"> Camera 1: <span id ="cam1"></span> </th>
    <th class="statusText"> Camera 2: <span id = "cam2"></span>  </th>;
    </tr >

    <!-- // Vị trí -->
    <tr style = "background-color: gray;">
    <th class="latandlong"> Vĩ độ: <span id = "latitude"></span></th>
    <th class="latandlong"> Kinh độ:  <span id = "longtitude"></span></th>
    </tr >

    <!-- // Trạng thái cửa -->
    <tr style = "background-color: gray;">
    <th class="statusText"> Cửa trước: <span id = "frontDoorStatus"></span></th>
    <th class="statusText"> Cửa sau:  <span id = "rearDoorStatus"></span></th>
    </tr >
    </table>

</body>
</html>