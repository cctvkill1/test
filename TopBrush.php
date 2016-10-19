 <?php
 set_time_limit(18000) ;
 function rand_ip(){
  $ip_long = array(
    array('607649792', '608174079'), 
    array('975044608', '977272831'), 
    array('999751680', '999784447'), 
    array('1019346944', '1019478015'), 
    array('1038614528', '1039007743'), 
    array('1783627776', '1784676351'), 
    array('1947009024', '1947074559'), 
    array('1987051520', '1988034559'), 
    array('2035023872', '2035154943'), 
    array('2078801920', '2079064063'), 
    array('-1950089216', '-1948778497'), 
    array('-1425539072', '-1425014785'), 
    array('-1236271104', '-1235419137'), 
    array('-770113536', '-768606209'), 
    array('-569376768', '-564133889'), 
    );
  $rand_key = mt_rand(0, 14);
  $huoduan_ip= long2ip(mt_rand($ip_long[$rand_key][0], $ip_long[$rand_key][1]));
  return $huoduan_ip;
}
function top($param){ 
  $ip = rand_ip();
  $headers['CLIENT-IP'] = $ip; 
  $headers['X-FORWARDED-FOR'] = $ip;  

  $headerArr = array(); 
  foreach( $headers as $n => $v ) { 
   $headerArr[] = $n .':' . $v;  
 }
 
 ob_start();
 $ch = curl_init();
 curl_setopt ($ch, CURLOPT_POST, 1 );
 curl_setopt ($ch, CURLOPT_URL, "http://115.28.115.64/top_list_v2/update_score");
 curl_setopt ($ch, CURLOPT_HTTPHEADER , $headerArr );  
 curl_setopt ($ch, CURLOPT_REFERER, "http://www.163.com/ ");   
 curl_setopt ($ch, CURLOPT_HEADER, 1);
 curl_setopt ($ch, CURLOPT_POSTFIELDS, $param);     
 $result        = curl_exec($ch);
 curl_close($ch); 
 var_dump($result);
 return $result; 
}
function sock_post($param){   
  $fp    = fsockopen('115.28.115.64', 80, $errno, $errstr, 8);  
  $head  = "POST /top_list_v2/update_score HTTP/1.1\r\n"; 
  $head .= "Host: 115.28.115.64\r\n";  
  $head .= "Content-type: application/x-www-form-urlencoded\r\n"; 
  $head .= "Content-Length: ".strlen(trim($param))."\r\n"; 
  $head .= "Connection: Keep-Alive\r\n"; 

  $head .= "\r\n"; 
  $head .= trim($param); 
  $write = fputs($fp, $head); 
  while (!feof($fp)) 
  {  
    $line = fread($fp,4096); 
    echo $line; 
  } 
}

function getSignature($str, $key="/TzSbON46vSq88gJyzosplEIoDyMpssbFDCj&") {  
  $signature = "";  
  if (function_exists('hash_hmac')) {  
    $signature = base64_encode(hash_hmac("sha1", $str, $key, true));  
  } else {  
    $blocksize = 64;  
    $hashfunc = 'sha1';  
    if (strlen($key) > $blocksize) {  
      $key = pack('H*', $hashfunc($key));  
    }  
    $key  = str_pad($key, $blocksize, chr(0x00));  
    $ipad = str_repeat(chr(0x36), $blocksize);  
    $opad = str_repeat(chr(0x5c), $blocksize);  
    $hmac = pack(  
      'H*', $hashfunc(  
        ($key ^ $opad) . pack(  
          'H*', $hashfunc(  
            ($key ^ $ipad) . $str  
            )  
          )  
        )  
      );  
    $signature = base64_encode($hmac);  
  }  
  return $signature;  
} 
 
$data=array(
"push_id"=>"111111111222222223333333344444444",
"market"=>"AppStroe",
"platform"=>1,
"version"=>"2.1",
"sid"=>"9a8026fceff32368e1a1a4ef218707d5",
"length"=>"163912",
"game_mode"=>1,
"uid"=>"936bb05d-6f48-4efd-9224-ba92bcb322dd",
"push_channel"=>1,
"name"=>"唐乾东出名了",
"version_code"=>"2128",
"channel"=>"AppStroe",
"device_id"=>"357458046556279",
"kill"=>14023,
);

ksort($data);
$str="";
foreach($data as $k=>$v)
{
  $str.="&".$k."=".$v;
}
$str="POST&top_list_v2/update_score".$str;
$data["snake_sign"]=getSignature($str);

// $result=Utility::HttpPost("http://115.28.115.64/top_list_v2/update_score",$data);
// var_dump($result);
top($data);
exit;
 



?>
