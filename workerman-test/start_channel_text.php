<?php
use Workerman\Worker;
require_once __DIR__ . '/vendor/autoload.php';     
require_once __DIR__ . '/vendor/workerman/Channel/src/Client.php';   

// 用来处理http请求，向任意客户端推送数据，需要传workerID和connectionID
// $http_worker = new Worker('http://0.0.0.0:4237');
$inner_text_worker  = new Worker('Text://0.0.0.0:4237');
$inner_text_worker ->name = 'publisher';
$inner_text_worker ->onWorkerStart = function()
{
    Channel\Client::connect('127.0.0.1', 2206);
};
$inner_text_worker ->onMessage = function($connection, $data)
{ 
    $data = json_decode($data);   
    $content = json_decode($data->content,true);  
    if(!$content)
        return; 
    $content = D_Function::FLush($content);
    if(isset($data->to_worker_id) && isset($data->to_uid))
    {
        $event_name = $data->to_worker_id;
        $to_uid = $data->to_uid;   
        Channel\Client::publish($event_name, array(
            'to_uid' => $to_uid,
            'content'          => $content
            ));
        $connection->send('push-ok');
    }
    else if(isset($data->broadcast))
    {
        $event_name = 'broadcast'; 
        Channel\Client::publish($event_name, array(
            'content'          => $content
            ));
        $connection->send('broadcast-ok');
    }
    $connection->send('no msg');
};


Worker::runAll();