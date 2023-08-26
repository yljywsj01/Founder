<?php
$host = 'localhost';
$dbuser = 'root';
$dbpassword = '';
$dbname = 'data';
$link = mysqli_connect($host, $dbuser, $dbpassword, $dbname);

if ($link) {
    mysqli_query($link, 'SET NAMES utf8');
} else {
    echo "不正確連接資料庫</br>" . mysqli_connect_error();
}

$datas = array();
$sql = "SELECT `item_id`, `item_picture`, `item_where`, `item_final` ,`item_or` FROM `item_pic_db` AS userData WHERE `item_type`= '2' ";

$result = mysqli_query($link, $sql);

if ($result) {
    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            $datas[] = $row;
        }
    }
    mysqli_free_result($result);
} else {
    echo "{$sql} 語法執行失敗，錯誤訊息: " . mysqli_error($link);
}

mysqli_close($link);

echo json_encode($datas); // 將資料以 JSON 格式返回
?>
