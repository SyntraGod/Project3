<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đổi thông tin xe</title>
</head>
<body>
    <h1 style="text-align: center; color: red">Thay đổi thông tin xe</h1>
    <form action="Form.php" method="POST">
        <div class="Don-vi-quan-ly">
            <label for="DVQL"> Đơn vị quản lý: </label>
            <input type="text" class="DVQL-Text" name="DVQL">
        </div>
        <div class="Tuyen">
            <label for="tuyen"> Tuyến : </label>
            <input type="text" class="Tuyen-text" name="tuyen">
        </div>
        <div class="Bien-kiem-soat">
            <label for="BKS"> Biển kiểm soát : </label>
            <input type="text" class="BKS-text" name="BKS">
        </div>
        <input type="submit"></input>
    </form>
</body>
</html>