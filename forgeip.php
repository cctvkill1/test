<?php  
$ip = "1.2.3.4";
$proxy = '87.203.241.151';
$proxyPort = '80';
$header = array(
	"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    // "Accept-Encoding:gzip, deflate, sdch",
	"Accept-Language:zh-CN,zh;q=0.8",
	"Connection:keep-alive",
	"Host:192.168.31.149",
	"Upgrade-Insecure-Requests:1",    
	"User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1", 
    "CLIENT-IP:".$proxy,
    "X-FORWARDED-FOR:".$proxy
	);
$ch = curl_init(); 
curl_setopt($ch,CURLOPT_URL, "http://wp.zhongyulian.com/checkip.php");
// curl_setopt($ch,CURLOPT_REFERER, "http://192.168.31.149:8006");  

curl_setopt($ch,CURLOPT_PROXYTYPE, CURLPROXY_HTTP);
curl_setopt($ch,CURLOPT_PROXY, $proxy.":".$proxyPort);  
// curl_setopt($ch,CURLOPT_HTTPPROXYTUNNEL, 1);

// curl_setopt($ch, CURLOPT_PROXYAUTH, CURLAUTH_BASIC); //代理认证模式
// curl_setopt($ch, CURLOPT_PROXY, "119.254.84.90"); //代理服务器地址
// curl_setopt($ch, CURLOPT_PROXYPORT, 80); //代理服务器端口
// //curl_setopt($ch, CURLOPT_PROXYUSERPWD, ":"); //http代理认证帐号，username:password的格式
// curl_setopt($ch, CURLOPT_PROXYTYPE, CURLPROXY_HTTP); //使用http代理模式

curl_setopt($ch,CURLOPT_HEADER, 1);   
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
  // curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);  
  // curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);  
curl_setopt($ch,CURLOPT_MAXREDIRS,20);  
curl_setopt($ch,CURLOPT_FOLLOWLOCATION, 1); 
curl_setopt($ch,CURLOPT_HTTPHEADER , $header );    
curl_setopt($ch,CURLOPT_USERAGENT,'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1');     
$result = curl_exec($ch);
var_dump($result);
curl_close ($ch); 
?>