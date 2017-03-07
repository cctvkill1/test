<?php
namespace GatewayWorker\Common;   

class ZhihuSpider{

	//获取关注者列表
	public static  function getUserFollow($username,$page=1){
		echo $username.PHP_EOL; 
		if(!$username)
			return ;   
		// $result =  \Spider\Cache\Db::query(' SELECT users.id,users.username,users.avatar,users.gender,users.`key` FROM users WHERE users.username = "test" ;');
		// var_dump($result);
		// exit;
		
		$url = "http://www.zhihu.com/people/{$username}/following?page={$page}"; 
		// echo $url.PHP_EOL;   
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
			for ($i=1; $i < $totalPage; $i++) {
				//workerman 异步处理
				$page++;  
				$arr = array('type'=>'getUserFollow','username'=>$username,'page'=>$page); 
				echo json_encode($arr);
				// $client = stream_socket_client('tcp://192.168.31.149:7273'); 
				// fwrite($client, json_encode($arr)."\n");  
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
			$data[]          = $row;
			// var_dump($row);
			//查这个关注者 workerman 异步处理
			$arr = array('type'=>'getUserFollow','username'=>$key,'page'=>1); 
			echo json_encode($arr);
			// $client = stream_socket_client('tcp://192.168.31.149:7273'); 
			// fwrite($client, json_encode($arr)."\n"); 
		} 
		return $data;
	}

} 