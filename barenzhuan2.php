 <?php
set_time_limit(1800); 
 $pagestartime=microtime(); 
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
		$this->result = array();
		$this->book   = array(); 
		$all          = array(1,2,3,4,5,6,7,8);  
		$this->rs     = $this->getAllPerm($all); 
		$this->flag   = true;
	}	
	//全队列 （1~8 以1开头的）
	function getAllPerm($all){
		$rs = array();  
		$last = count($all) - 1; 
		$z = 0; 
		$x = $last; 
		$rs[] = $all; 
		while($x > 0 && $all[0]==1) 
		{ 
			$y = $x--; 
			if($all[$x] < $all[$y]) 
			{
				$z = $last; 
				while($all[$x] > $all[$z]) 
				{ 
					$z--; 
				} 
				list($all[$x], $all[$z]) = array($all[$z], $all[$x]); 
				for($i = $last; $i > $y; $i--, $y++) 
				{ 
					list($all[$i], $all[$y]) = array($all[$y], $all[$i]); 
				} 
				$rs[] = $all; 
				$x = $last; 
			} 
		} 
		return $rs; 
	} 
 	//统计每个人的对手数量
	function totalNum(){  
		$this->rivalFlag = false;
		$this->teammateFlag = false;
		$result = $this->result;
		for ($x = 0; $x < count($result); $x++) { 
			for ($y = 0; $y < 8 ; $y++) { 
				$t = $result[$x][$y];
				$z = $y/2;
				switch ($z) {
					case 0: 
					$t1 = $result[$x][2];
					$t2 = $result[$x][3];
					$t3 = $result[$x][0];
					$t4 = $result[$x][1];
					break; 
					case 1: 
					$t1 = $result[$x][0];
					$t2 = $result[$x][1]; 
					$t3 = $result[$x][2];
					$t4 = $result[$x][3];
					break; 
					case 2: 
					$t1 = $result[$x][6];
					$t2 = $result[$x][7];
					$t3 = $result[$x][4];
					$t4 = $result[$x][5]; 
					break; 
					case 3: 
					$t1 = $result[$x][4];
					$t2 = $result[$x][5]; 
					$t3 = $result[$x][6];
					$t4 = $result[$x][7];
					break; 
				}
				if($t1&&$t2&&$t3&&$t4){
					$tArr[$t][$t1]++;
					$tArr[$t][$t2]++;
					if($t!=$t3)
						$teamArr[$t][$t3]++;
					if($t!=$t4)
						$teamArr[$t][$t4]++;
					if($tArr[$t][$t1]>2){
						$this->rivalFlag = true;
						break 2;
					}
					if($tArr[$t][$t2]>2){
						$this->rivalFlag = true;
						break 2;
					}
					if($teamArr[$t][$t3]>1){
						$this->teammateFlag = true;
						break 2;
					}
					if($teamArr[$t][$t4]>1){						
						$this->teammateFlag = true;
						break 2;
					}
				}
			}
		}
		// $this->tArr = $tArr;
	}
	//从新计算缓存数组
	function calcTotal(){
		$result = $this->result;
		$cArr   = array();
		for ($x = 0; $x < count($result); $x++) { 
			$cArr[] = $result[$x]; 
		}
		$this->cArr = $cArr; 
	}
 	//depth-first-search
	function dfs($step=0){ 
		if($step==2) return $this->result; 
		if($this->book[$step] == 1) continue;
		// echo $step."<br>";
		// if($step>6){  
		for ($i=0; $i < 8; $i++) {
			for ($j=0; $j < 8; $j++) {
				echo $this->result[$i][$j].' ';
			}
			echo "<br>";
		}
		// } 
		$rs     = $this->rs; 
		$this->calcTotal();
		$cArr = $this->cArr;
		// echo $step.'--';
		$tt = $this->result[count($this->result)-1];
		for ($k=0; $k < count($rs); $k++) {
			$temp = $rs[$k];
			if($tt&&$tt[1]>=$temp[1])continue; 
			if($tt&&$tt[1]<$temp[1]-1) continue;
			if(in_array($temp,$cArr))continue;
			// var_dump($temp);echo "<br>";
			$this->result[$step] = $temp; 
			$this->totalNum(); 
			$rivalFlag    = $this->rivalFlag; 
			$teammateFlag = $this->teammateFlag;  
			// echo $step;
			// var_dump($rivalFlag);
			// var_dump($teammateFlag);
			// echo "<br>";
			if($teammateFlag||$rivalFlag){
				array_pop($this->result);
				// array_splice($this->result, $step,1);
				continue;
			}  
			// var_dump($temp);echo "<br>";
			// var_dump($this->result);
			// echo "<br>";
			// echo $step;
			$this->book[$step] = 1;
			$this->dfs($step+1);
			$this->book[$step] = 0;  
			$this->calcTotal();
			$cArr = $this->cArr;
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


$pageendtime = microtime(); 
$starttime   = explode(" ",$pagestartime); 
$endtime     = explode(" ",$pageendtime); 
$totaltime   = $endtime[0]-$starttime[0]+$endtime[1]-$starttime[1]; 
$timecost 	 = sprintf("%s",$totaltime*1000);  
echo "<br>运行时间: $timecost 毫秒<br>"; 
?>