<?php
use Workerman\Worker;
require_once __DIR__ . '/vendor/autoload.php';    
require_once __DIR__ . '/vendor/workerman/Channel/src/Server.php';  

// 初始化一个Channel服务端
$channel_server = new Channel\Server('0.0.0.0', 2206);
 
Worker::runAll();