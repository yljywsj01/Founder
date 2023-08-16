<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>失物招領</title>
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
    <script>
        function refreshData() {
            var selectedOption = document.getElementById("filter").value;
            var imageContainer = document.getElementById("imageContainer");
            
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "your_page.php?filter=" + selectedOption, true);
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    imageContainer.innerHTML = xhr.responseText;
                }
            };
            xhr.send();
        }
    </script>
</head>
<body>
    <h1>Which is your cloth?</h1>
    <select id="filter" onchange="refreshData()">
        <option value="today">今天</option>
        <option value="3days">三天內</option>
        <option value="1week">一週內</option>
        <option value="1month">一個月內</option>
        <option value="all">全部資料</option>
    </select>
    <div id="imageContainer">
    <?php
    $host = 'localhost';
    $dbuser ='root';
    $dbpassword = '';
    $dbname = 'data';
    $link = mysqli_connect($host, $dbuser, $dbpassword, $dbname);
    if ($link) {
        mysqli_query($link, 'SET NAMES utf8');
        echo "正確連接資料庫";
    } else {
        echo "不正確連接資料庫</br>" . mysqli_connect_error();
    }

    // 設置一個空陣列來放資料
    $datas = array();

    // 獲取下拉選單的值
    //$selectedOption = $_POST['filter']; // 假設使用POST方法提交表單
    if (isset($_GET['filter'])) {
        $selectedOption = $_GET['filter'];
    } else {
        $selectedOption = 'all'; // 預設顯示全部資料
    }

    // 根據下拉選單的值來修改SQL查詢語句
    switch ($selectedOption) {
        case 'today':
            $sql = "SELECT `item_id`, `item_picture`, `item_where`, `item_final`, `item_or` FROM `item_pic_db` AS userData WHERE `item_type` = '2' AND DATE(`item_final`) = CURDATE()";
            break;
        case '3days':
            $sql = "SELECT `item_id`, `item_picture`, `item_where`, `item_final`, `item_or` FROM `item_pic_db` AS userData WHERE `item_type` = '2' AND `item_final` >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)";
            break;
        case '1week':
            $sql = "SELECT `item_id`, `item_picture`, `item_where`, `item_final`, `item_or` FROM `item_pic_db` AS userData WHERE `item_type` = '2' AND `item_final` >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK)";
            break;
        case '1month':
            $sql = "SELECT `item_id`, `item_picture`, `item_where`, `item_final`, `item_or` FROM `item_pic_db` AS userData WHERE `item_type` = '2' AND `item_final` >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)";
            break;
        default:
            $sql = "SELECT `item_id`, `item_picture`, `item_where`, `item_final`, `item_or` FROM `item_pic_db` AS userData WHERE `item_type` = '2'";
            break;
    }
    
    function getValue($selectedOption) {
        alert($selectedOption.value);
    }

    // 用mysqli_query方法執行(sql語法)將結果存在變數中
    $result = mysqli_query($link, $sql);

    // 如果有資料
    if ($result) {
        // mysqli_num_rows方法可以回傳我們結果總共有幾筆資料
        if (mysqli_num_rows($result) > 0) {
            // 取得大於0代表有資料
            // while迴圈會根據資料數量，決定跑的次數
            // mysqli_fetch_assoc方法可取得一筆值
            $i = mysqli_num_rows($result) - 1;
            while ($row = mysqli_fetch_assoc($result)) {
                // 每跑一次迴圈就抓一筆值，最後放進data陣列中
                $datas[] = $row;
            }
        }
        // 釋放資料庫查到的記憶體
        mysqli_free_result($result);
    } else {
        echo "{$sql} 語法執行失敗，錯誤訊息: " . mysqli_error($link);
    }

    // 處理完後印出資料
    if (!empty($result)) {
        // 如果結果不為空，就利用print_r方法印出資料

        //print_r($datas);
        //$img = $_POST[""]

        //echo mysqli_num_rows($result);

        //echo $sql;
        echo '<div class="row">';
        while ($i >= 0) {
            $domain =  $datas[$i]['item_picture'];
            $num = $datas[$i]['item_id'];
            $item_where = $datas[$i]['item_where'];
            $item_final = $datas[$i]['item_final'];

            if ($item_final == "若無移動 輸入原位即可") {
                $item_final = $item_where;
            }

            echo '<div class="image-container">';
            echo '<img src="'.$domain.'">';
            //echo '<div>'.$num.'</div>';
            echo '<div>遺失處: '.$item_where.'</div>';
            echo '<div>最後放置於: '.$item_final.'</div>';
            echo '</div>';

            $i = $i - 1;
        }
        echo '</div>';

        /*$domain =  $datas[0]['item_picture'];
        echo $domain;
        echo '<img src="'.$domain.'">';*/

        /*foreach($datas as $pic){
            header("Content-Type: image/png");
            header("Content-Length: " . strlen($pic));
            fpassthru($pic);
            echo strlen($pic);
        }*/

        //print_r($datas);
    } else {
        // 為空表示沒資料
        echo "查無資料";
    }
    ?></div>
</body>
</html>
