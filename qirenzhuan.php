 <?php  
 //七人转 
//优化是个问题哦 速度太慢了
 $pagestartime=microtime(); 
 $all = array(1,2,3,4,5,6,7);
 $count = count($all);
 for ($i=1; $i <= $count ; $i++) { 
 	for ($j=$i+1; $j <=$count ; $j++) { 
 		$arr[] = $i*10+$j;
 	}
 } 
//后3.5会死循环 出不来结果
 function changeReusult($result,$tArr,$arr,$count,$countR){ 
 	$cArr = array();
 	shuffle($arr);
 	$arrCount = count($arr);
 	$cArr[] = $result[10][0]*10+$result[10][1];  
 	// for ($i=$countR; $i < $count*2; $i++) { 
 	// 	for ($j=0; $j < 4; $j++) { 
 	// 		$result[$i][$j] = 0;
 	// 	}
 	// } 
 	for ($i=$countR; $i < $countR+4; $i++) {
 		for ($j=($i==$countR?1:0); $j < 2; $j++) {
 			for ($k=0; $k <  $arrCount; $k++) {
 				$temp = $arr[$k];
 				$t1 = intval($temp/10);
 				$t2 = $temp % 10;
 				if(!in_array($temp,$cArr)&&!in_array($t1,$result[$i])&&!in_array($t2,$result[$i])&&$dArr[$t1]<2&&$dArr[$t2]<2){
 					$y = count($result[$i]);
 					$z = $y/2;
 					if($z==1){
 						$x1 = $result[$i][0];
 						$x2 = $result[$i][1]; 
 						$flag = $tArr[$temp][$x1]>=$tArr[$temp][$x2]?$tArr[$temp][$x1]:$tArr[$temp][$x2]; 
 						if($flag>=1) continue; 
 					} 
 					$cArr[] = $temp;
 					$result[$i][] = $t1;
 					$result[$i][] = $t2;
 					$dArr[$t1]++;
 					$dArr[$t2]++;
 					break; 
 				}
 			} 
 		}  
 		//记录对手次数
 		for ($x = $i; $x < $i+1; $x++) {
 			$x1 = $result[$x][0];
 			$x2 = $result[$x][1];
 			$x3 = $result[$x][2];
 			$x4 = $result[$x][3];  
 			if($x1&&$x2&&$x3&&$x4){
 				$tArr[$x1*10+$x2][$x3]++;
 				$tArr[$x1*10+$x2][$x4]++; 
 				$tArr[$x3*10+$x4][$x1]++;
 				$tArr[$x3*10+$x4][$x2]++;  
 			}
 		}
 	}  
 	$isOk = true; 
 	for ($i=0; $i < $count*2; $i++) {
 		for ($j=0; $j < 4; $j++) { 
 			if(!$result[$i][$j]){
 				$isOk = false;
 				break 2;
 			}
 		}
 	} 
 	if(!$isOk){
 		$result = changeReusult($result,$tArr,$arr,$count,$countR);  		
 		return $result;
 	} 
 	return $result;
 }
 function recursion($arr,$count){
 	$result = $cArr = $tArr = $dArr = array();
 	$arrCount = count($arr);
 	for ($i=0; $i < $count*2; $i++) {
 		for ($j=0; $j < 2; $j++) {
 			for ($k=0; $k < $arrCount; $k++) {
 				$temp = $arr[$k];
 				$t1 = intval($temp/10);
 				$t2 = $temp % 10;
 				if(!in_array($temp,$cArr)&&!in_array($t1,$result[$i])&&!in_array($t2,$result[$i])){   					
 					$cArr[] = $temp;		
 					$result[$i][] = $t1;
 					$result[$i][] = $t2;
 					break;
 				}
 			} 
 		} 
 		//记录对手次数
 	}
 	$countR = 10;
 	for ($x=0; $x < 10; $x++) {
 		$x1 = $result[$x][0];
 		$x2 = $result[$x][1];
 		$x3 = $result[$x][2];
 		$x4 = $result[$x][3];  
 		if($x1&&$x2&&$x3&&$x4){
 			$tArr[$x1*10+$x2][$x3]++;
 			$tArr[$x1*10+$x2][$x4]++; 
 			$tArr[$x3*10+$x4][$x1]++;
 			$tArr[$x3*10+$x4][$x2]++;  
 		}
 	}

 	// $result = array(
 	// 	1 2 3 4 
 	// 	1 3 2 4 
 	// 	1 4 2 3 
 	// 	1 5 2 6 
 	// 	1 6 2 5 
 	// 	1 7 3 5 
 	// 	2 7 3 6 
 	// 	3 7 4 5 
 	// 	4 6 5 7 
 	// 	4 7 5 6 
 	// 	6 7
 	// 	);

	//上面生成了10.5对阵
	//再增加3.5个对阵  

 	// $result = changeReusult($result,$tArr,$arr,$count,$countR);

 	$cArr = array();
 	shuffle($arr);
 	$arrCount = count($arr);
 	$cArr[] = $result[10][0]*10+$result[10][1];  
 	// for ($i=$countR; $i < $count*2; $i++) { 
 	// 	for ($j=0; $j < 4; $j++) { 
 	// 		$result[$i][$j] = 0;
 	// 	}
 	// } 
 	for ($i=$countR; $i < $countR+4; $i++) {
 		for ($j=($i==$countR?1:0); $j < 2; $j++) {
 			for ($k=0; $k <  $arrCount; $k++) {
 				$temp = $arr[$k];
 				$t1 = intval($temp/10);
 				$t2 = $temp % 10;
 				if(!in_array($temp,$cArr)&&!in_array($t1,$result[$i])&&!in_array($t2,$result[$i])&&$dArr[$t1]<2&&$dArr[$t2]<2){
 					$y = count($result[$i]);
 					$z = $y/2;
 					if($z==1){
 						$x1 = $result[$i][0];
 						$x2 = $result[$i][1]; 
 						$flag = $tArr[$temp][$x1]>=$tArr[$temp][$x2]?$tArr[$temp][$x1]:$tArr[$temp][$x2]; 
 						if($flag>=1) continue; 
 					} 
 					$cArr[] = $temp;
 					$result[$i][] = $t1;
 					$result[$i][] = $t2;
 					$dArr[$t1]++;
 					$dArr[$t2]++;
 					break; 
 				}
 			} 
 		}  
 		//记录对手次数
 		for ($x = $i; $x < $i+1; $x++) {
 			$x1 = $result[$x][0];
 			$x2 = $result[$x][1];
 			$x3 = $result[$x][2];
 			$x4 = $result[$x][3];  
 			if($x1&&$x2&&$x3&&$x4){
 				$tArr[$x1*10+$x2][$x3]++;
 				$tArr[$x1*10+$x2][$x4]++; 
 				$tArr[$x3*10+$x4][$x1]++;
 				$tArr[$x3*10+$x4][$x2]++;  
 			}
 		}
 	}  
 	$isOk = true; 
 	for ($i=0; $i < $count*2; $i++) {
 		for ($j=0; $j < 4; $j++) { 
 			if(!$result[$i][$j]){
 				$isOk = false;
 				break 2;
 			}
 		}
 	} 
 	if(!$isOk){
 		// $result = changeReusult($result,$tArr,$arr,$count,$countR);
 		$result = recursion($arr,$count);  		
 		return $result;
 	} else {
 		//一个组合的单个对手出现一次
 		for ($x=0; $x < count($result); $x++) {
 			$x1 = $result[$x][0];
 			$x2 = $result[$x][1];
 			$x3 = $result[$x][2];
 			$x4 = $result[$x][3];  
 			if($x1&&$x2&&$x3&&$x4){
 				$test[$x1*10+$x2][$x3]++;
 				$test[$x1*10+$x2][$x4]++; 
 				$test[$x3*10+$x4][$x1]++;
 				$test[$x3*10+$x4][$x2]++;  
 				// $testAll[$x1]++;
 				// $testAll[$x2]++;
 				// $testAll[$x3]++;
 				// $testAll[$x4]++;
 			}
 		}
 		// 这个判断有点多余
 		// foreach ($testAll as $key => $value) {
 		// 	foreach ($value as $k => $v) { 
 		// 		if($v!=8){
 		// 			$isOk = false;
 		// 			break 2;
 		// 		}
 		// 	}
 		// }
 		// if(!$isOk){
 		// 	$result = recursion($arr,$count);  
 		// 	return $result;
 		// }else{
 		foreach ($test as $key => $value) {
 			foreach ($value as $k => $v) { 
 				if($v>1){
 					$isOk = false;
 					break 2;
 				}
 			}
 		}
 		if(!$isOk){
 			// $result = changeReusult($result,$tArr,$arr,$count,$countR);
 			$result = recursion($arr,$count);  		
 			return $result;
 		}else  
 		return $result;
 		// }
 	}
 }
 //测试得到更多的数组
 function getAll($arr,$count,$i,$allR=array()){
 	if($i>15){
 		return $allR;
 	}
 	$result = recursion($arr,$count); 
 	if(!in_array($result,$allR)){ 
 		$allR[] = $result;
 		$i++;
 	}
 	return	getAll($arr,$count,$i,$allR);
 }

//输出最后的对阵数组（每个人不能连续出现3次）
 function endResult($arr,$count){
 	$testAll = array();
 	for ($i=1; $i <8 ; $i++) {
 		$testAll[$i] = 0;
 	}

 	$result = recursion($arr,$count);  
 	for ($i=0; $i < $count*2; $i++) {  
 		$x1 = $result[$i][0];
 		$x2 = $result[$i][1];
 		$x3 = $result[$i][2];
 		$x4 = $result[$i][3];  
 		$flag = 1;
 		if($testAll[$x1]>=2) 
 			$flag=0;
 		if($testAll[$x2]>=2) 
 			$flag=0;
 		if($testAll[$x3]>=2)
 			$flag=0;
 		if($testAll[$x4]>=2) 
 			$flag=0;
		// var_dump($result[$i]);
	 	// var_dump($testAll);
	 	// print_r($result[$i]);
 		if(!$flag){
 		// echo "error ";
 			for ($x=$i+1; $x < $count*2; $x++) { 
 				$flag1 = $flag2 = $flag3 = $flag4 = 1;
 				$xx1 = $result[$x][0];
 				$xx2 = $result[$x][1];
 				$xx3 = $result[$x][2];
 				$xx4 = $result[$x][3];  
 				if($testAll[$xx1]>=2) 
 					$flag1=0;
 				if($testAll[$xx2]>=2) 
 					$flag2=0;
 				if($testAll[$xx3]>=2)
 					$flag3=0;
 				if($testAll[$xx4]>=2) 
 					$flag4=0;
 				if($flag1&&$flag2&&$flag3&&$flag4){		
 					$temp = $result[$i];
 					$result[$i] = $result[$x];
 					$result[$x] = $temp ;   
 					$flag = 1;
 					break; 
 				}
 			}
 			if(!$flag){
 				$isReturn = 1;
 				break;
 			}
 		}

 		// var_dump($result[$i]);
 		$x1 = $result[$i][0];
 		$x2 = $result[$i][1];
 		$x3 = $result[$i][2];
 		$x4 = $result[$i][3];  
 		$testAll[$x1]++;
 		$testAll[$x2]++;
 		$testAll[$x3]++;
 		$testAll[$x4]++; 
 		$testAll[$x1]=$testAll[$x1]>=3?0:$testAll[$x1]; 
 		$testAll[$x2]=$testAll[$x2]>=3?0:$testAll[$x2]; 
 		$testAll[$x3]=$testAll[$x3]>=3?0:$testAll[$x3]; 
 		$testAll[$x4]=$testAll[$x4]>=3?0:$testAll[$x4]; 
 		for ($j=0; $j <8 ; $j++) {
 			if($j!=$x1&&$j!=$x2&&$j!=$x3&&$j!=$x4) 
 				$testAll[$j] = 0; 		
 		}
 		// print_r($testAll);
 	}
 	if($isReturn)
 		$result = endResult($arr,$count);
 	return $result;
 }

//运气好20MS 平均2000MS
 // $result = recursion($arr,$count); 
 //太慢咯 运气好30多秒 运气不好超时
 $result = endResult($arr,$count);

 for ($i=0; $i < $count*2; $i++) {  
 	for ($j=0; $j < 4; $j++) {  
 		echo $result[$i][$j].' ';
 	}  
 	echo "<br>";
 }

 // $allR = getAll($arr,$count,0); 
 // foreach ($allR as $key => $result) {  	
 // 	for ($i=0; $i < $count*2; $i++) { 
 // 		for ($j=0; $j < 4; $j++) { 
 // 			if($j==2)echo ": ";
 // 			echo $result[$i][$j].' ';
 // 		}
 // 		echo "<br>";
 // 	}
 // 	echo "=============================<br>";
 // }
 



 $pageendtime = microtime(); 
 $starttime   = explode(" ",$pagestartime); 
 $endtime     = explode(" ",$pageendtime); 
 $totaltime   = $endtime[0]-$starttime[0]+$endtime[1]-$starttime[1]; 
 $timecost 	 = sprintf("%s",$totaltime*1000);  
 echo "<br>运行时间: $timecost 毫秒<br>";   
 // echo "<br>平均时间: ".($timecost/10)." 毫秒<br>"; 
 ?>