 <?php  
  set_time_limit(1800) ;
 function postVote($ip){ 
 	$headers['CLIENT-IP'] = $ip; 
 	$headers['X-FORWARDED-FOR'] = $ip;

 	$headerArr = array(); 
 	foreach( $headers as $n => $v ) { 
 		$headerArr[] = $n .':' . $v;  
 	}
 	$data = array(      
 		'action'=>'JudgeIP',
 		'id'=>18
 		);      
 	ob_start();
 	$ch = curl_init();
 	curl_setopt ($ch, CURLOPT_URL, "http://cjqk.kawasakijp.com/ajax/vote.ashx?date=".(time()+rand()%10));
 	curl_setopt ($ch, CURLOPT_HTTPHEADER , $headerArr );  
 	curl_setopt ($ch, CURLOPT_REFERER, "http://www.163.com/ ");   
 	curl_setopt( $ch, CURLOPT_HEADER, 1);
 	curl_setopt($ch, CURLOPT_POSTFIELDS, $data);      
 	curl_exec($ch);
 	curl_close ($ch); 
 }

 
 $ipFile = 'D:/ip2.txt';
 $filename ="D:/use-ip2.txt";

 $file = file($ipFile);
 foreach($file as &$line) {
 $use = file_get_contents($filename);
 	if(strpos($use, $line)===false){
 		$s = explode(':', $line);
 		for ($i=0; $i < 5; $i++) { 		
 			postVote($s[0]); 
 		}
 		$handle=fopen($filename,"a+"); 
 		$str=fwrite($handle,$line."\n"); 
 		fclose($handle);

 	}  
 }


 echo "over";
 ?>