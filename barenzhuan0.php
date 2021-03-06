 <?php 
 /*
1 2 3 4 5 6 7 8 
1 3 5 7 2 4 6 8 
1 4 2 3 5 8 6 7 
1 5 2 6 3 7 4 8 
1 6 2 5 3 8 4 7 
1 7 3 5 4 6 2 8 
1 8 4 5 2 7 3 6
 */
//八人转
class baren{
 	//构造函数
	function __construct($count = 8){
		$this->count = $count; 
		for ($i=1; $i <= $count ; $i++) { 
			for ($j=$i+1; $j <=$count ; $j++) { 
				$arr[] = $i*10+$j;
			}
		}
		$this->arr    = $arr;
		$this->result = array();
		$this->cArr   = array();
		$this->tArr   = array(); 
		$this->book   = array(); 
	}
 	//统计每个人的对手数量
	function totalNum($step){ 
		$i = intval(($step-1)/4); 
		$result = $this->result;
		for ($x = 0; $x < count($result); $x++) { 
			for ($y = 0; $y < 8 ; $y++) { 
				$t = $result[$x][$y];
				$z = $y/2;
				switch ($z) {
					case 0: 
					$t1 = $result[$i][2];
					$t2 = $result[$i][3];
					break; 
					case 1: 
					$t1 = $result[$i][0];
					$t2 = $result[$i][1]; 
					break; 
					case 2: 
					$t1 = $result[$i][6];
					$t2 = $result[$i][7]; 
					break; 
					case 3: 
					$t1 = $result[$i][4];
					$t2 = $result[$i][5]; 
					break; 
				}
				if($t1&&$t2){
					$tArr[$t][$t1]++;
					$tArr[$t][$t2]++;
				}
			}
		}
		$this->tArr = $tArr;
	}
	//从新计算缓存数组
	function calcTotal(){
		$result = $this->result;
		$cArr   = array();
		for ($x = 0; $x < count($result); $x++) { 
			for ($y = 0; $y < 4 ; $y++) { 
				$i = $result[$x][$y*2];
				$j = $result[$x][$y*2+1];
				if($i&&$j){
					if(!in_array($i*10+$j, $cArr))
						$cArr[] = $i*10+$j; 
				}
			}
		}
		$this->cArr = $cArr;
		// var_dump($cArr);
	}
 	//depth-first-search
	function dfs($step=1){
		if($step==count($this->arr)) return $this->result;
		if($this->book[$step]==1) return;
 		// var_dump($step);
		// if($step>10){
		for ($i=0; $i < 8; $i++) {
			for ($j=0; $j < 8; $j++) {
				echo $this->result[$i][$j].' ';
			}
			echo "<br>";
		}
		// }
		$i = intval(($step-1)/4);
		$j = ($step-1)%4;
		$arr    = $this->arr;
		$result = $this->result;
		$this->totalNum();
		$tArr   = $this->tArr;
		$this->calcTotal();
		$cArr = $this->cArr;
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
					$flag1 = $tArr[$x1][$t1]>=$tArr[$x2][$t1]?$tArr[$x1][$t1]:$tArr[$x2][$t1];
					$flag2 = $tArr[$x1][$t2]>=$tArr[$x2][$t2]?$tArr[$x1][$t2]:$tArr[$x2][$t2];
				}else if($z==3){
					$x1 = $result[$i][4];
					$x2 = $result[$i][5];
					$flag1 = $tArr[$x1][$t1]>=$tArr[$x2][$t1]?$tArr[$x1][$t1]:$tArr[$x2][$t1];
					$flag2 = $tArr[$x1][$t2]>=$tArr[$x2][$t2]?$tArr[$x1][$t1]:$tArr[$x2][$t2];
				}
				$flag = $flag1>=$flag2?$flag1:$flag2;
 				// var_dump($flag);
				// if($flag>=1) continue;	
				if($flag>=2) continue;						
				$this->book[$step] = 1;
				$this->result[$i][$j*2] = $t1;
				$this->result[$i][$j*2+1] = $t2;
				// echo $i.'-'.$j;
				// print_r($this->result);
				// echo "<br>";
				$this->dfs($step+1);
				$this->book[$step] = 0; 
				$this->calcTotal();
				$cArr = $this->cArr;
				$this->totalNum();
				$tArr = $this->tArr;
			}
		} 
	}

	function show(){
		var_dump($this->dfs());
	}

}
$barenArr = array(
	0 => array(1,2,3,4,5,6,7,8),
	1 => array(1,3,5,7,2,4,6,8),
	2 => array(1,4,6,7,2,3,5,8),
	3 => array(1,5,2,6,3,7,4,8),
	4 => array(1,6,3,8,2,5,4,7),
	5 => array(1,7,2,8,3,5,4,6),
	6 => array(1,8,4,5,2,7,3,6),
	);
echo "标准答案<br>";
for ($i=0; $i < 8; $i++) { 
	for ($j=0; $j < 8; $j++) { 
		echo $barenArr[$i][$j].' ';
	}
	echo "<br>";
}
$baren = new baren(); 
$baren->show();
?>