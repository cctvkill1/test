<?php
namespace Common;   
use \Common\Functions;

class ZhihuSpider{

	public static $pdo = null; 
	public static $ip  = null; 
	public static $port = null; 
	public static $i = 1; 


	//获取关注者列表
	public static  function getUserFollow($username,$page=1){
		if(!$username)
			return ;    
		//test
		$max = self::$i+10;
		for (; self::$i < $max; self::$i++) { 
			$arr = array('type'=>'getUserFollow','username'=>self::$i,'page'=>self::$i); 			
			echo Functions::udate('H:i:s.u')."---". json_encode($arr).PHP_EOL;
			$client = stream_socket_client('tcp://'.self::$ip.':'.self::$port); 
			fwrite($client, json_encode($arr)."\n"); 
		}
		return;
		$result = self::$pdo -> query('select * from users where username="'.$username.'"');   
		if($result -> fetch()) 
			return;
		$url = "http://www.zhihu.com/people/{$username}/following?page={$page}"; 
		$res = self::curlGet($url);
		//第一页
		$userInfo = self::getUserInfo($res);
		if($page==1){
			//获取data并转义 再分析数据 查出总页数
			preg_match('<div id="data" style="display:none;" data-state="(.*?)".*?>', $res, $out); 
			$_data     = empty($out[1]) ? '' : $out[1];
			$_data     = htmlspecialchars_decode($_data);
			$_data     = json_decode($_data,true);		
			$totals    = intval($_data['people']['followingByUser'][$username]['totals']);
			$totalPage = $totals%20==0?intval($totals/20):intval($totals/20)+1;
			//第二页到最后一页
			for ($i=2; $i < $totalPage; $i++) {
				//workerman 异步处理 
				$arr = array('type'=>'getUserFollow','username'=>$username,'page'=>$i); 
				// echo Functions::udate('H:i:s.u')."---". json_encode($arr).PHP_EOL;
				$client = stream_socket_client('tcp://'.self::$ip.':'.self::$port); 
				fwrite($client, json_encode($arr)."\n"); 

			} 
		}
	}

	public static function curlGet($url){
		$ch = curl_init($url); 
		curl_setopt($ch, CURLOPT_HEADER, false);
		curl_setopt($ch, CURLOPT_USERAGENT,  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36"); 
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 15); 
		curl_setopt($ch, CURLOPT_TIMEOUT, 25);  
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);  
		curl_setopt($ch, CURLOPT_MAXREDIRS, 3);  
		// curl_setopt($ch, CURLOPT_ENCODING, 'gzip');  
		curl_setopt($ch, CURLOPT_REFERER, 'http://www.zhihu.com');  	

		$r = curl_exec($ch); 
		curl_close($ch);
		return $r;
	} 
	//获取所有关注者的信息
	public static function getUserInfo($content){
		$data = array(); 
		if (empty($content))  
			return $data; 		
		preg_match('<div id="data" style="display:none;" data-state="(.*?)".*?>', $content, $out); 
		$_data = empty($out[1]) ? '' : $out[1];
		$_data = htmlspecialchars_decode($_data);
		$_data = json_decode($_data,true);		
		if(!$_data)return $data;
		foreach ($_data['entities']['users'] as $key => $value) { 
			$avatarUrl       = str_replace('_is', '_xl', $value['avatarUrl']); 
			$row             = array();
			$row['key']      = $key;
			$row['username'] = $value['name']; 
			$row['gender']   = intval($value['gender']);
			$row['avatar']   = $avatarUrl;
			//插入数据库
			// $data[]          = $row; 
			if(self::$pdo -> exec("insert into users(username,`key`,gender,avatar) values('".$row['username']."','".$row['key']."',".$row['gender'].",'".$row['avatar'] ."')"))  
				echo   Functions::udate('H:i:s.u')."---".$row['key']." insert successful".PHP_EOL; 
			//查这个关注者 workerman 异步处理
			$arr = array('type'=>'getUserFollow','username'=>$key,'page'=>1); 
			// echo Functions::udate('H:i:s.u')."---". json_encode($arr).PHP_EOL;
			$client = stream_socket_client('tcp://'.self::$ip.':'.self::$port); 
			fwrite($client, json_encode($arr)."\n"); 
		} 
		return $data;
	}

} 