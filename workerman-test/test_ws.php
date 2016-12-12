<?php 
$pagestartime=microtime(); 
use \Workerman\Worker; 
use \Workerman\Autoloader; 
use Workerman\Connection\AsyncTcpConnection; 
use Workerman\Lib\Timer; 

require_once __DIR__ . '/vendor/autoload.php';  

$arr=array( 
  "opt"=>5,"cmd"=>"login",  
  // "UserId"=>11008,  
  // 'WeixinId'=>'ojIJ0wZlUMu2iqF1whaZ1qkjZaag'
  'OpenId' => '5358d6941bf9353b00db0641114c4832',
  "unic_key" => 'tuyi12xx4t5222g986rc9bz9vji62s41',

  ); 

$worker = new Worker();

$worker->onWorkerStart = function($worker){

    // 以websocket协议连接远程websocket服务器
 $ws_connection = new AsyncTcpConnection('ws://127.0.0.1:4236');
    // 连上后发送hello字符串
 $ws_connection->onConnect = function($connection){

  global $arr;
  global $pagestartime; 
  $pagestartime=microtime();  
  $str = D_Function::FLush($arr); 
    // $iv =Utility::makeIv();
    // $str=gzcompress(bson_encode($arr));
    // $str=$iv.Utility::McryptStr($str,$iv);   
    // $pagestartime=microtime();  
  $connection->send($str); 
    // $connection->send('hello');
};
    // 远程websocket服务器发来消息时
$ws_connection->onMessage = function($connection, $data){
 global $arr;
 global $pagestartime;
 $pagestartime=microtime();  
 echo "from server msg:";
   // var_dump($data);   
 $x = D_Function::DecodeInput($data); 

 $pageendtime = microtime(); 
 $starttime   = explode(" ",$pagestartime); 
 $endtime     = explode(" ",$pageendtime); 
 $totaltime   = $endtime[0]-$starttime[0]+$endtime[1]-$starttime[1]; 
 $timecost    = $totaltime*1000;   
 echo "运行时间: $timecost 毫秒\n"; 
 var_dump($x); 
};
    // 连接上发生错误时，一般是连接远程websocket服务器失败错误
$ws_connection->onError = function($connection, $code, $msg){
  echo "error: $msg\n";
};
    // 当连接远程websocket服务器的连接断开时
$ws_connection->onClose = function($connection){
  echo "connection closed\n";
};
    // 设置好以上各种回调后，执行连接操作
$ws_connection->connect(); 

Timer::add(9, function()use($ws_connection){
 $str = D_Function::FLush(array('msg_type'=>'ping'));  
 $ws_connection->send($str); 
  // foreach($worker->connections as $connection) {
  //   $str = D_Function::FLush(array('msg_type'=>'ping')); 
  //   $connection->send($str);
  // }
});

};

Worker::runAll();

