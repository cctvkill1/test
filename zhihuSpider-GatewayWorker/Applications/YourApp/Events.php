<?php
/**
 * This file is part of workerman.
 *
 * Licensed under The MIT License
 * For full copyright and license information, please see the MIT-LICENSE.txt
 * Redistributions of files must retain the above copyright notice.
 *
 * @author walkor<walkor@workerman.net>
 * @copyright walkor<walkor@workerman.net>
 * @link http://www.workerman.net/
 * @license http://www.opensource.org/licenses/mit-license.php MIT License
 */

/**
 * 用于检测业务代码死循环或者长时间阻塞等问题
 * 如果发现业务卡死，可以将下面declare打开（去掉//注释），并执行php start.php reload
 * 然后观察一段时间workerman.log看是否有process_timeout异常
 */

/**
 * BusinessWorker::$processTimeout 属性需要配合declare(ticks=1)才能生效(windows无效)
 */ 
// declare(ticks=1);

use \GatewayWorker\Lib\Gateway;
use \GatewayWorker\Common\Functions;
use \GatewayWorker\Common\ZhihuSpider;

// 自动加载类
// require_once __DIR__ . '/../../vendor/autoload.php';

/**
 * 主逻辑
 * 主要是处理 onConnect onMessage onClose 三个方法
 * onConnect 和 onClose 如果不需要可以不用实现并删除
 */
class Events
{

    /**
     * 当客户端连接时触发
     * 如果业务不需此回调可以删除onConnect
     * 
     * @param int $client_id 连接id
     */
    public static function onConnect($client_id)
    {
        // 向当前client_id发送数据 
      Gateway::sendToClient($client_id, "Hello $client_id\r\n");
        // 向所有人发送
      Gateway::sendToAll("$client_id login\r\n");
    }
    
   /**
    * 当客户端发来消息时触发
    * @param int $client_id 连接id
    * @param mixed $message 具体消息
    */
   public static function onMessage($client_id, $message)
   {
    $req_data = json_decode($message, true);
    echo Functions::udate('H:i:s.u')."---".$message."\r\n";
    if($req_data['type']=='getUserFollow'){
       ZhihuSpider::getUserFollow($req_data['username'],intval($req_data['page']));
    } 

  }


   /**
    * 当用户断开连接时触发
    * @param int $client_id 连接id
    */
   public static function onClose($client_id)
   {
       // 向所有人发送 
     GateWay::sendToAll("$client_id logout\r\n");
   }
 }
