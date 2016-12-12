<?php
require_once __DIR__ . '/vendor/autoload.php';   
use \Workerman\Worker; 
use \Workerman\Autoloader;
use Workerman\Protocols\Websocket; 
use Workerman\Lib\Timer;  
require_once __DIR__ . '/vendor/workerman/Channel/src/Client.php';   
require_once "service.define.php";

// 心跳间隔25秒
define('HEARTBEAT_TIME', 10);
// websocket服务端
$worker = new Worker('websocket://0.0.0.0:4236');
$worker->count = 1;
$worker->name  = 'workers';
$connection_count = 0;
$worker->onWorkerStart = function($worker)
{ 
    // Channel客户端连接到Channel服务端
    Channel\Client::connect('127.0.0.1', 2206);
    // 以自己的进程id为事件名称
    // $event_name = $worker->id; 
    $event_name = 0; 
    // 订阅worker->id事件并注册事件处理函数
    Channel\Client::on($event_name, function($event_data)use($worker){
        $to_uid = $event_data['to_uid'];
        $message = $event_data['content'];
        foreach($worker->connections as $connection){
            if(isset($connection->uid)&&$connection->uid ==$to_uid){
                $to_connection = $connection;
                break;
            }
        }
        if(!isset($to_connection)){
            echo "connection not exists\n";
            return;
        } 
        echo "----send msg----\n"; 
        $to_connection->websocketType = Websocket::BINARY_TYPE_ARRAYBUFFER; 
        $to_connection->send($message);
    });

    // 订阅广播事件
    $event_name = 'broadcast';
    // 收到广播事件后向当前进程内所有客户端连接发送广播数据
    Channel\Client::on($event_name, function($event_data)use($worker){
        $message = $event_data['content']; 
        echo "====send broadcast====\n"; 
        foreach($worker->connections as $connection)
        {
            $connection->websocketType = Websocket::BINARY_TYPE_ARRAYBUFFER; 
            $connection->send($message);
        }
    });

    // 进程启动后设置一个每秒运行一次的定时器
    Timer::add(1, function()use($worker){
        $time_now = time();
        foreach($worker->connections as $connection) {
            // 有可能该connection还没收到过消息，则lastMessageTime设置为当前时间
            if (empty($connection->lastMessageTime)) {
                $connection->lastMessageTime = $time_now;
                continue;
            }
            // 上次通讯时间间隔大于心跳间隔，则认为客户端已经下线，关闭连接
            if ($time_now - $connection->lastMessageTime > HEARTBEAT_TIME) {
                $connection->close();
            }
        }
    });
    echo "******** server is started ********\n";
};

$worker->onConnect = function($connection)use($worker)
{ 
    global $connection_count;
    ++$connection_count;  
    echo $worker->id.'---'.$connection->id."(".$connection_count.")Connection successful(".$connection->getRemoteIp().") \n";   
};
$worker->onClose = function($connection)use($worker)
{ 
    global $connection_count;
    ++$connection_count; 
    echo $worker->id.'==='.$connection->id."(".$connection_count.")disconnect(".$connection->getRemoteIp().") \n";   
};
$worker->onMessage = function($connection,$data)use($worker)
{
    // 给connection临时设置一个lastMessageTime属性，用来记录上次收到消息的时间
    $connection->lastMessageTime = time();
    ob_start();
    $connection->websocketType = Websocket::BINARY_TYPE_ARRAYBUFFER; 
    $data     = D_Function::DecodeInput($data);  
    if($data['msg_type']=='ping') {
        $result = array('msg_type'=>'pong');
        $result = D_Function::Flush($result);  
        ob_end_clean();
    }else{
        $result   = Framer::Run(new F_BsonFramer(new F_Service(),$data)); 
        $r = $result;
        if($result['cmd']=='login'&&$result['opt']==5){  
            $connection->uid = intval($result['info']['UserId']); 
            $r['cid'] = $connection->id;
            $r['uid'] = $connection->uid;
        }  
        $result = D_Function::Flush($result);  
        ob_end_clean();
        echo json_encode($r)."\n";
    }
    if($result)
        $connection->send($result);

};

Worker::runAll();