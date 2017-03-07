<?php
use \Workerman\Worker;
use \Workerman\WebServer;
use \GatewayWorker\Gateway;
use \GatewayWorker\BusinessWorker;
use \Workerman\Autoloader;
require_once __DIR__ . '/../../vendor/autoload.php'; 


$internal_gateway = new Gateway("Text://0.0.0.0:7273");
$internal_gateway->name='internalGateway';
$internal_gateway->startPort = 2800;
$internal_gateway->registerAddress = '192.168.31.149:1238';
// #### 内部推送端口设置完毕 ####

if(!defined('GLOBAL_START'))
{
    Worker::runAll();
}