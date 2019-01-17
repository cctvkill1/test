<?php

ini_set("display_errors", "On");
error_reporting(E_ALL | E_STRICT);

$id = intval($_GET['id']);
$movies = json_decode(file_get_contents('movies.json'),true); 
$movie = $movies[$id]; 
?>

<!DOCTYPE HTML>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <title><?php echo $movie['title'];?> 田聪的私人影院</title> 
    <link href="css/video-js.min.css" rel="stylesheet">
<style>
    body{
        background: #000;
    }
    .title{
        font-size: 28px;
        color: #fff;
        padding: 50px 40px;
    }
    #video{
        width: 100%;
        height: auto;
    }
    .tip{
        color: #fff;
    }
</style>
</head>
<body> 
<p class="tip">建议在wifi下观看！网速稍慢，耐心等待！</p>
<script type="text/javascript" src="js/ckplayer.min.js"></script>
<div id="video"></div>
<script type="text/javascript">
	var videoObject = {
        poster:"image/<?php echo $movie['img'];?>",
		container: '#video',//“#”代表容器的ID，“.”或“”代表容器的class
		variable: 'player',//该属性必需设置，值等于下面的new chplayer()的对象
		flashplayer:false,//如果强制使用flashplayer则设置成true
		video:"movies/<?php echo $movie['m3u8'];?>"//视频地址
	};
	var player=new ckplayer(videoObject);
</script>
 
    
</body>

</html>