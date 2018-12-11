 <?php 
 set_time_limit(1800);
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
function brush($ip,$proxy){    
  $header = array(
    "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    // "Accept-Encoding:gzip, deflate, sdch",
    "Accept-Language:zh-CN,zh;q=0.8",
    "Connection:keep-alive",
    "Host:115.28.115.64",
    "Upgrade-Insecure-Requests:1",    
    "User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1", 
    "CLIENT-IP:".$ip,
    "X-FORWARDED-FOR:".$ip
    );
 // var_dump($header);exit; 
  $ch = curl_init(); 
  $rnd = mt_rand(0,999999)/1000000; 
  curl_setopt($ch,CURLOPT_URL, "http://v2.10brandchina.com/api/weixin/sdk.php?url=http://m.10brandchina.com/vote/startin.php?id=40467~rnd=".$rnd);
  // curl_setopt($ch,CURLOPT_REFERER, "http://123.57.242.67");  
  curl_setopt($ch,CURLOPT_PROXYTYPE, CURLPROXY_HTTP);
  // curl_setopt($ch,CURLOPT_PROXY, $proxy);  
  curl_setopt($ch,CURLOPT_HEADER, 1);   
  curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
  // curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);  
  // curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);  
  curl_setopt($ch,CURLOPT_MAXREDIRS,20);  
  curl_setopt($ch,CURLOPT_FOLLOWLOCATION, 1); 
  curl_setopt($ch,CURLOPT_HTTPHEADER , $header );    
  curl_setopt($ch,CURLOPT_USERAGENT,'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1');     
  $result = curl_exec($ch);
  // var_dump($result);
  curl_close ($ch); 
}
 
for ($i=0; $i <100 ; $i++) {  
 $ip  = rand_ip();  
        echo $ip.PHP_EOL;
        brush($ip,null); 
//  $handle = @fopen("proxy.txt", "r");
// if ($handle) {
//     while (!feof($handle)) {
//         $proxy = fgets($handle, 4096);
//         // echo $proxy.'<br>';
//         brush($ip,$proxy); 
//     }
//     fclose($handle);
// }
 // usleep(10000);   
 // sleep(1);
}
echo "over";  
?>
