<?php
    $DVQL = "N/A";
    $Tuyen = "N/A";
    $BKS = "N/A";
   // $file = fopen("BusInfor.txt","a");
   $file  = "D:\Document\Year5\Project3\Data-Processing\Web\BusInfor.txt" ; // Replace 'your_file.txt' with your file name or path

   // Check if the file exists
   if (file_exists($file)) {
       // Open the file
       $handle = fopen($file, 'r');
   
       $num = 0;
       // Read the file line by line
       while (!feof($handle)) {
           $data = fgets($handle);
           if($data == '')  continue;
           // Tách chuỗi thành mảng các phần tử bằng ký tự '/'
            $dataArray = explode('/', $data);

            $DVQL = $dataArray[0];
            $Tuyen = $dataArray[1];
            $BKS = $dataArray[2];
       }
   
       // Close the file handle
       fclose($handle);
   } else {
       echo "File does not exist.";
   }
   
?>