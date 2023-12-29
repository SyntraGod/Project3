<?php
$sql = "SELECT idBUS, numIn, numOut, timeBus, statusBus FROM Bus WHERE idBUS = '0001'";
$result = $conn->query($sql);

    // Số khách vào / ra
    echo "<tr >";
    echo " <th style=\"background-color: green;\">Số khách vào</th>";
    echo " <th style=\"background-color: red;\"> Số khách ra</th>";
    echo "</tr>";    
    //In ra số hành khách
    if ($result->num_rows > 0) {
      $row = $result->fetch_assoc();
      echo "<tr>";
      $curPassenger = $row["numIn"] - $row["numOut"];
      $doorStatus = "Close";
      if ($row["statusBus"] == 0) $doorStatus = "Open"; 
      echo "<th>" . $row["numIn"] . "</th>";
      echo "<th>" . $row["numOut"] . "</th>";
      echo "</tr>";
    }

    // Số hành khách hiện tại
    echo "<tr >";
    echo " <th style=\"background-color: #ffcc00;\" , colspan = \"2\">Số khách trên xe</th>";
    echo "</tr>";   
    echo "<th colspan = \"2\">" . $curPassenger . "</th>";

    // Trạng thái Camera
    echo "<tr style = \"background-color: gray;\">";
    echo "<th> Camera 1: ON </th>";
    echo "<th> Camera 2: OFF </th>";
    echo "</tr >";

    // Trạng thái cửa
    echo "<tr style = \"background-color: gray;\">";
    echo "<th> Cửa trước: " . $doorStatus . "</th>";
    echo "<th> Cửa sau: Close </th>";
    echo "</tr >";

$conn->close();
?>