<?php
use Workerman\Worker;
require_once __DIR__ . '/vendor/autoload.php';     
require_once __DIR__ . '/vendor/workerman/Channel/src/Client.php';   

// 用来处理http请求，向任意客户端推送数据，需要传workerID和connectionID
$http_worker = new Worker('http://0.0.0.0:4237');
$http_worker->name = 'publisher';
$http_worker->onWorkerStart = function()
{
    Channel\Client::connect('127.0.0.1', 2206);
};
$http_worker->onMessage = function($connection, $data)
{
    $connection->send('ok');
    if(empty($_GET['content'])) return;
    // 是向某个worker进程中某个连接推送数据
    if(isset($_GET['to_worker_id']) && isset($_GET['to_connection_id']))
    {
        $event_name = $_GET['to_worker_id'];
        $to_connection_id = $_GET['to_connection_id'];
        $content = $_GET['content'];
        Channel\Client::publish($event_name, array(
           'to_connection_id' => $to_connection_id,
           'content'          => $content
        ));
    }
    // 是全局广播数据
    else
    {
        $event_name = '广播';
        $content = $_GET['content'];
        Channel\Client::publish($event_name, array(
           'content'          => $content
        ));
    }
};


Worker::runAll();