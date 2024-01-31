<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đổi thông tin xe</title>
    <style>
        form{
            width: 80%;
            border: 1px solid;
            margin-left: auto;
            margin-right: auto;
        }
        label{
            width: 100%;
            margin-left: 100px;
            font-weight: bold;
        }
        label{
            font-size: 22px;
        }
        .DVQL-Text, .Tuyen-text, .BKS-Text{
            margin-top: 10px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 500px;
            height: 30px;
            font-size: 20px;
        }
        .submit-btn{
            margin-top: 10px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            font-size: 20px;
            margin-bottom: 20px;
        }
    </style>
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
            <input type="text" class="BKS-Text" name="BKS">
        </div>
        <input type="submit" class="submit-btn"></input>
    </form>
</body>
</html>