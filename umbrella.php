<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>失物招領</title>
</head>
<body>
    <h1>Which is your umbrella?</h1>
    <?php
    $host = 'localhost';
    $dbuser ='root';
    $dbpassword = '';
    $dbname = 'data';
    $link = mysqli_connect($host,$dbuser,$dbpassword,$dbname);
    if($link){
        mysqli_query($link,'SET NAMES utf8');
        //echo "正確連接資料庫";
    }
    else {
        echo "不正確連接資料庫</br>" . mysqli_connect_error();
    }

    // 設置一個空陣列來放資料
    $datas = array();
    // sql語法存在變數中
    $sql = "SELECT `item_id`, `item_picture`, `item_where`, `item_final` ,`item_or` FROM `item_pic_db` AS userData WHERE `item_type`= '3' ";

    // 用mysqli_query方法執行(sql語法)將結果存在變數中
    $result = mysqli_query($link,$sql);

    // 如果有資料
    if ($result) {
        // mysqli_num_rows方法可以回傳我們結果總共有幾筆資料
        if (mysqli_num_rows($result)>0) {
            // 取得大於0代表有資料
            // while迴圈會根據資料數量，決定跑的次數
            // mysqli_fetch_assoc方法可取得一筆值
            $i=mysqli_num_rows($result)-1;
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
        
        //print_r($datas);
        //$img = $_POST[""]
        
        //echo mysqli_num_rows($result);
        
        //echo $sql;
        while ( $i>=0) {
            $domain =  $datas[$i]['item_picture'];
            $num = $datas[$i]['item_id'];
            $item_where = $datas[$i]['item_where'];
            $item_final = $datas[$i]['item_final'];

            if($item_final=="若無移動 輸入原位即可"){
                $item_final = $item_where;
            }
            
            //echo $domain;
            echo '<div>';
            echo '<img src="'.$domain.'" style="max-width: 500px; max-height: 500px;">';
            echo '<div>遺失處: '.$item_where.'</div>';
            echo '<div>最後放置於: '.$item_final.'</div>';
            echo '</div>';
            echo '<br>';
            $i=$i-1;
        }
    }
    else {
        // 為空表示沒資料
        echo "查無資料";
    }
    ?>
</body>
</html>
