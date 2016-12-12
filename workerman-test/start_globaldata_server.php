<?php
use Workerman\Worker;
require_once __DIR__ . '/vendor/autoload.php';    
require_once __DIR__ . '/vendor/workerman/GlobalData/src/Server.php';  

// 初始化一个GlobalData服务端
$worker = new GlobalData\Server('0.0.0.0', 2207);
 
Worker::runAll();