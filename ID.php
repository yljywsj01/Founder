<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>IDACRD</title>
    <style>
        .image-container {
            display: inline-block;
            text-align: center;
            margin: 10px;
        }

        .image-container img {
            max-width: 500px;
            max-height: 500px;
        }
    </style>
</head>
<body>

<?php
// 取得使用者輸入字串
$num = $_POST["num"];

$host = 'localhost';
$dbuser = 'root';
$dbpassword = '';
$dbname = 'data';
$link = mysqli_connect($host, $dbuser, $dbpassword, $dbname);

if ($link) {
    mysqli_query($link, 'SET NAMES utf8');
    echo "正確連接資料庫<br>";

    // 查詢資料庫，找到與使用者輸入相符的資料
    $query = "SELECT * FROM `item_pic_db` WHERE id_num = '$num'";
    $result = mysqli_query($link, $query);

    if ($result) {
        if (mysqli_num_rows($result) > 0) {
            echo "匹配到的資料：<br>";
            while ($row = mysqli_fetch_assoc($result)) {
                $domain = $row['item_picture'];
                $num = $row['item_id'];
                $item_where = $row['item_where'];
                $item_final = $row['item_final'];
                $item_name = $row['id_name'];
    
                if ($item_final == "若無移動 輸入原位即可") {
                    $item_final = $item_where;
                }
                
                echo '<div class="image-container">';
                echo '<img src="' . $domain . '">';
                echo '<div>您的姓名：' . $item_name . '</div>';
                echo '<div>遺失處：' . $item_where . '</div>';
                echo '<div>最後放置於：' . $item_final . '</div>';
                echo '</div>';
            }
        } else {
            echo "找不到匹配的資料。";
        }
    } else {
        echo "查詢資料庫時出現問題：" . mysqli_error($link);
    }
} else {
    echo "不正確連接資料庫<br>" . mysqli_connect_error();
}
?>

</body>
</html>
