 <?php   
//八人转
 $all = array(1,2,3,4,5,6,7,8);
 $count = 8;
 for ($i=1; $i <= $count ; $i++) { 
 	for ($j=$i+1; $j <=$count ; $j++) { 
 		$arr[] = $i*10+$j;
 	}
 }
 $result = $cArr = $tArr = array();
 for ($i=0; $i < $count; $i++) { 
 		$tt = 0;
 	for ($j=0; $j < 4; $j++) {   
 		for ($k=0; $k < count($arr); $k++) {
 			$temp = $arr[$k];
 			if($temp>$tt){
 				$t1 = intval($temp/10);
 				$t2 = $temp % 10;
 				if(!in_array($temp,$cArr)&&!in_array($t1,$result[$i])&&!in_array($t2,$result[$i])){
 					$y = count($result[$i]);
 					$z = $y/2;
 					if($z==1){
 					$tt = $t2*10;
 						$x1 = $result[$i][0];
 						$x2 = $result[$i][1];
 						$flag1 = $tArr[$x1][$t1]>=$tArr[$x2][$t1]?$tArr[$x1][$t1]:$tArr[$x2][$t1];
 						$flag2 = $tArr[$x1][$t2]>=$tArr[$x2][$t2]?$tArr[$x1][$t2]:$tArr[$x2][$t2];
 					}else if($z==3){
 						$x1 = $result[$i][4];
 						$x2 = $result[$i][5];
 						$flag1 = $tArr[$x1][$t1]>=$tArr[$x2][$t1]?$tArr[$x1][$t1]:$tArr[$x2][$t1];
 						$flag2 = $tArr[$x1][$t2]>=$tArr[$x2][$t2]?$tArr[$x1][$t1]:$tArr[$x2][$t2];
 					}
 					$flag = $flag1>=$flag2?$flag1:$flag2;
 					
 					if($flag>=1) continue;
 					$cArr[] = $temp;
 					$result[$i][] = $t1;
 					$result[$i][] = $t2;
 					break;
 				}
 			}
 		}

 	}
	//记录对手次数
 	for ($x = $i; $x < $i+1; $x++) { 
 		for ($y = 0; $y < 8 ; $y++) { 
 			$t = $result[$x][$y];
 			$z = $y/2;
 			switch ($z) {
 				case 0: 
 				$t1 = $result[$i][2];
 				$t2 = $result[$i][3];
 				$tArr[$t][$t1]++;
 				$tArr[$t][$t2]++;
 				break; 
 				case 1: 
 				$t1 = $result[$i][0];
 				$t2 = $result[$i][1];
 				$tArr[$t][$t1]++;
 				$tArr[$t][$t2]++;
 				break; 
 				case 2: 
 				$t1 = $result[$i][6];
 				$t2 = $result[$i][7];
 				$tArr[$t][$t1]++;
 				$tArr[$t][$t2]++;
 				break; 
 				case 3: 
 				$t1 = $result[$i][4];
 				$t2 = $result[$i][5];
 				$tArr[$t][$t1]++;
 				$tArr[$t][$t2]++;
 				break; 
 			}
 		}
 	}
 	// var_dump($tArr);
 }

 for ($i=0; $i < $count; $i++) { 
 	for ($j=0; $j < 4; $j++) {   
 		for ($k=0; $k < count($arr); $k++) { 
 			$temp = $arr[$k];
 			$t1 = intval($temp/10);
 			$t2 = $temp % 10;
 			if(!in_array($temp,$cArr)&&!in_array($t1,$result[$i])&&!in_array($t2,$result[$i])){
 				$y = count($result[$i]);
 				$z = $y/2;
 				if($z==1){
 					$x1 = $result[$i][0];
 					$x2 = $result[$i][1];
 					$flag = $tArr[$x1][$t1]>=$tArr[$x2][$t1]?$tArr[$x1][$t1]:$tArr[$x2][$t1];
 				}else if($z==3){
 					$x1 = $result[$i][4];
 					$x2 = $result[$i][5];
 					$flag = $tArr[$x1][$t1]>=$tArr[$x2][$t1]?$tArr[$x1][$t1]:$tArr[$x2][$t1];
 				}
 				// var_dump($temp);
 				// // var_dump($x1);
 				// // var_dump($x2);
 				// // var_dump($tArr[$x1][$t1]);
 				// // var_dump($tArr[$x2][$t1]);
 				// var_dump($flag);
 				// // var_dump($result[$i]);
 				// echo "<br>";
 				if($flag>=2) continue;
 				$cArr[] = $temp;
 				$result[$i][] = $t1;
 				$result[$i][] = $t2;
 			}
 		}

 	}
	//记录对手次数 第一次循环只出来2横排
 	if($i>2){
 		for ($x = $i; $x < $i+1; $x++) { 
 			for ($y = 0; $y < 8 ; $y++) { 
 				$t = $result[$x][$y];
 				$z = $y/2;
 				switch ($z) {
 					case 0: 
 					$t1 = $result[$i][2];
 					$t2 = $result[$i][3];
 					$tArr[$t][$t1]++;
 					$tArr[$t][$t2]++;
 					break; 
 					case 1: 
 					$t1 = $result[$i][0];
 					$t2 = $result[$i][1];
 					$tArr[$t][$t1]++;
 					$tArr[$t][$t2]++;
 					break; 
 					case 2: 
 					$t1 = $result[$i][6];
 					$t2 = $result[$i][7];
 					$tArr[$t][$t1]++;
 					$tArr[$t][$t2]++;
 					break; 
 					case 3: 
 					$t1 = $result[$i][4];
 					$t2 = $result[$i][5];
 					$tArr[$t][$t1]++;
 					$tArr[$t][$t2]++;
 					break; 
 				}
 			}
 		}
 	}
 }

 // print_r($result);
 for ($i=0; $i < 7; $i++) { 
 	for ($j=0; $j < 8; $j++) { 
 		echo $result[$i][$j].' ';
 	}
 	echo "<br>";
 }
 

 ?>