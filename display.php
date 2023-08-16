<title>Clothes_Check</title>
<meta http-equiv="content-type" charset="UTF-8"/>

<!--找圖片-->
<?php
    $host = 'localhost';
    $dbuser ='root';
    $dbpassword = '';
    $dbname = 'data';
    $link = mysqli_connect($host,$dbuser,$dbpassword,$dbname);
    if($link){
        mysqli_query($link,'SET NAMES utf8');
        echo "正確連接資料庫";
    }
    else {
            echo "不正確連接資料庫</br>" . mysqli_connect_error();
    }

    // 設置一個空陣列來放資料
    $datas = array();
    // sql語法存在變數中
    $sql = "SELECT `item_type`, FROM `item_pic_db` AS userData WHERE `item_type`='2' ";

    // 用mysqli_query方法執行(sql語法)將結果存在變數中
    $result = mysqli_query($link,$sql);
    // 如果有資料
    if ($result) {
        // mysqli_num_rows方法可以回傳我們結果總共有幾筆資料
        if (mysqli_num_rows($result)>0) {
            // 取得大於0代表有資料
            // while迴圈會根據資料數量，決定跑的次數
            // mysqli_fetch_assoc方法可取得一筆值
            while ($row = mysqli_fetch_assoc($result)) {
                // 每跑一次迴圈就抓一筆值，最後放進data陣列中
                $datas[] = $row;
            }
        }
        // 釋放資料庫查到的記憶體
        mysqli_free_result($result);
    }
    else {
        echo "{$sql} 語法執行失敗，錯誤訊息: " . mysqli_error($link);
    }
    // 處理完後印出資料
    if(!empty($result)){
        // 如果結果不為空，就利用print_r方法印出資料
        print_r($datas);
    }
    else {
        // 為空表示沒資料
        echo "查無資料";
    }
?>






