<title>File_Upload</title>
     <meta http-equiv="content-type" charset="UTF-8"/>

     <!--<h1>檔案上傳</h1>-->
         <?php
                        
            //取得上傳檔案資訊
            //$filename=$_FILES['my_file']['tmp_name'];
            $tmpname=$_FILES['my_file']['tmp_name'];
            $filetype=$_FILES['my_file']['type'];
            $filesize=$_FILES['my_file']['size'];
            
            $file=NULL;
            
            if(isset($_FILES['my_file']['error'])){    
                if($_FILES['my_file']['error']==0){                                    
                    $instr = fopen($tmpname,"rb" );
                    $file = addslashes(fread($instr,filesize($tmpname)));       
                    //echo $file; 
                }
            }
                            
            //$sql=sprintf("insert into item_pic_db(image)values(%s)","'".$file."'");


            $where = $_POST["where"];
            $final = $_POST["final"];
            $item = $_POST["item"];
               
            
            
            if(empty($where)){
                echo "where empty";
            }

            
            $dest = 'upload/' . $_FILES['my_file']['name'];    
            move_uploaded_file($tmpname, $dest);

            $host = 'localhost';
            $dbuser ='root';
            $dbpassword = '';
            $dbname = 'data';
            $link = mysqli_connect($host,$dbuser,$dbpassword,$dbname);
            if($link){
                mysqli_query($link,'SET NAMES utf8');
                echo "正確連接資料庫";

                $new_id= mysqli_insert_id ($link);
                $new_id++;
                $date=date('Y-m-d');
                $idname='';
                $idnum='';

                if($item==1){
                    $py = 'D:/xampp/htdocs/import_easyocr.py';
                    $command = "python $py $dest";

                    $output = array();
                    $status = 0;

                    exec($command, $output, $status);

                    echo "<pre>";
                    print_r($output);
                    echo "</pre>";

                    if ($status !== 0) {
                        // 執行錯誤，可以處理錯誤訊息或執行其他動作
                        echo "執行命令出錯，錯誤訊息：";
                        print_r($output);
                    } else {
                        $idname = $output[1]; // 將 Array[1] 存到 $idname
                        $idnum = $output[2]; // 將 Array[2] 存到 $idnum
                        
                        echo "姓名：$idname<br>";
                        echo "身分證字號：$idnum<br>";
                    }
                }

                $sql = sprintf("INSERT INTO  `item_pic_db`(`item_id`,`item_picture`, `item_where`, `item_finaL`, `item_type`, `item_or`, `item_date`, `id_name`, `id_num`)
                 VALUE(%d, %s, %s, %s, %s, '0', %s, %s, %s) ", "'".$new_id."'", "'".$dest."'", "'".$where."'", "'".$final."'", "'".$item."'", "'".$date."'", "'".$idname."'", "'".$idnum."'");

                // 用mysqli_query方法執行(sql語法)將結果存在變數中
                $result = mysqli_query($link,$sql);
                
                // 如果有異動到資料庫數量(更新資料庫)
                if (mysqli_affected_rows($link)>0) {
                // 如果有一筆以上代表有更新
                // mysqli_insert_id可以抓到第一筆的id
                $new_idd= mysqli_insert_id ($link);
                echo "新增後的id為 {$new_idd} ";
                }
                elseif(mysqli_affected_rows($link)==0) {
                    echo "無資料新增";
                }
                else {
                    echo "{$sql} 語法執行失敗，錯誤訊息: " . mysqli_error($link);
                }
                mysqli_close($link); 
            }
            else {
                echo "不正確連接資料庫</br>" . mysqli_connect_error();
            }


        ?>