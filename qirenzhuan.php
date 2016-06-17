 <?php 
 //七人转 
 $pagestartime=microtime(); 
 $all = array(1,2,3,4,5,6,7);
 $count = count($all);
 for ($i=1; $i <= $count ; $i++) { 
 	for ($j=$i+1; $j <=$count ; $j++) { 
 		$arr[] = $i*10+$j;
 	}
 } 


 function recursion($arr,$count){ 
 	$result = $cArr = $tArr = $dArr = array();
 	for ($i=0; $i < $count*2; $i++) {
 		for ($j=0; $j < 2; $j++) {
 			for ($k=0; $k < count($arr); $k++) {
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
 	$countR = count($result)-1;
 	for ($x=0; $x < count($result); $x++) {
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
 	// var_dump($tArr);echo "<br>";
	//上面生成了10.5对阵
	//再增加3.5个对阵 
 	$cArr = array();
 	shuffle($arr);
 	$cArr[] = $result[10][0]*10+$result[10][1];
 	for ($i=$countR; $i < $countR+4; $i++) { 	
 		for ($j=($i==$countR?1:0); $j < 2; $j++) {
 			for ($k=0; $k < count($arr); $k++) {
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
 		$result = recursion($arr,$count); 
 		return $result;
 	}else{ 
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
 				$result = recursion($arr,$count);  
 				return $result;
 			}else  
 			return $result;
 		// }
 	}
 }
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

 $allR = getAll($arr,$count,0); 
 foreach ($allR as $key => $result) {  	
 	for ($i=0; $i < $count*2; $i++) { 
 		for ($j=0; $j < 4; $j++) { 
 			if($j==2)echo ": ";
 			echo $result[$i][$j].' ';
 		}
 		echo "<br>";
 	}
 	echo "=============================<br>";
 }

 // $result = recursion($arr,$count); 
 // for ($i=0; $i < $count*2; $i++) { 
 // 	for ($j=0; $j < 4; $j++) { 
 // 		echo $result[$i][$j].' ';
 // 	}
 // 	echo "<br>";
 // }

 


 $pageendtime = microtime(); 
 $starttime   = explode(" ",$pagestartime); 
 $endtime     = explode(" ",$pageendtime); 
 $totaltime   = $endtime[0]-$starttime[0]+$endtime[1]-$starttime[1]; 
 $timecost 	 = sprintf("%s",$totaltime*1000);  
 echo "<br>运行时间: $timecost 毫秒<br>";   
 echo "<br>平均时间: ".($timecost/10)." 毫秒<br>"; 

 ?>