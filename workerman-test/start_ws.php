<?php  
use \Workerman\Worker; 
use \Workerman\Autoloader;
use Workerman\Protocols\Websocket;  
// 自动加载类
require_once __DIR__ . '/vendor/autoload.php';   

require_once "service.define.php";


// 初始化一个worker容器，监听1234端口
$worker = new Worker('websocket://0.0.0.0:7272');
/*
 * 注意这里进程数必须设置为1，否则会报端口占用错误
 * (php 7可以设置进程数大于1，前提是$inner_text_worker->reusePort=true)
 */

Worker::$stdoutFile = __DIR__.'/tmp/error.log';
$worker->count = 4;
// worker进程启动后创建一个text Worker以便打开一个内部通讯端口
$worker->onWorkerStart = function($worker)
{ 
    // 开启一个内部端口，方便内部系统推送数据，Text协议格式 文本+换行符
  $inner_text_worker = new Worker('text://0.0.0.0:5678');
  $inner_text_worker->onMessage = function($connection, $buffer)
  { 
    $data = json_decode($buffer, true);
      // $data数组格式，里面有uid，表示向那个uid的页面推送数据      
    $uid = $data['uid'];
    if($uid == 'all'){
     $ret = broadcast($data); 
     $connection->send('ok');
   }else if($uid){
       		 // 通过workerman，向uid的页面推送数据
     $ret = sendMessageByUid($uid, $data);
       		 // 返回推送结果
     $connection->send($ret ? 'ok' : 'fail');
   }
 };
    // ## 执行监听 ##
 $inner_text_worker->listen();

  echo "服务已经启动"; 
};
// 新增加一个属性，用来保存uid到connection的映射
$worker->uidConnections = array();

$worker->onConnect = function($connection)
{ 
  global $worker;
  $connection->uid = 1;   
  if($connection->uid){
   $worker->uidConnections[$connection->uid] = $connection;   
   echo '---'.$connection->uid."连接成功（".$connection->getRemoteIp()."）\n";  
 }
};
// 当有客户端发来消息时执行的回调函数
$worker->onMessage = function($connection, $data)
{ 
  $connection->websocketType = Websocket::BINARY_TYPE_ARRAYBUFFER;
  // var_dump($data);
  global $worker; 
    // 判断当前客户端是否已经验证,既是否设置了uid
	// if(!isset($connection->uid))
	// {
       // 没验证的话把第一个包当做uid（这里为了方便演示，没做真正的验证）
        $connection->uid = $connection->id;   
       /* 保存uid到connection的映射，这样可以方便的通过uid查找connection，
        * 实现针对特定uid推送数据
        */
       $worker->uidConnections[$connection->uid] = $connection; 
       $result = Framer::Run(new F_BsonFramer(new F_Service(),$data,$connection));  
       // var_dump($result);

       // $test = bson_encode($test);
       // var_dump($test);
       $ret = sendMessageByUid($connection->uid, $result); 
       return;
   // }
     };

// 当有客户端连接断开时
     $worker->onClose = function($connection)
     {
      global $worker;
      if(isset($connection->uid))
      {
        // 连接断开时删除映射
       unset($worker->uidConnections[$connection->uid]);
       echo '==='.$connection->uid."断开连接（".$connection->getRemoteIp()."）\n";  
     }
   };

// 向所有验证的用户推送数据
   function broadcast($message)
   {
   	global $worker;
   	foreach($worker->uidConnections as $connection)
   	{ 
   		$connection->send($message);
   	}
   }

// 针对uid推送数据
   function sendMessageByUid($uid, $message)
   {
   	global $worker;
   	if(isset($worker->uidConnections[$uid]))
   	{
   		$connection = $worker->uidConnections[$uid];
   		$connection->send($message);
   		return true;
   	}
   	return false;
   }

// 运行所有的worker
   Worker::runAll();

