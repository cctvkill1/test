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
    .video-js{
        width: 100%;
        height: auto;
    }
    .tip{
        color: #fff;
    }
</style>
</head>
<body> 
<p class="tip">建议在wifi下观看！初始加载要等一会！</p>
<video id="my-video" autoplay="autoplay"  class="video-js" controls preload="auto" poster="image/<?php echo $movie['img'];?>"  >
    <source src="movies/<?php echo $movie['m3u8'];?>" > 
    <p class="vjs-no-js">
        您的浏览器不支持 video 标签。
    </p>
  </video>

  <script src="js/video.min.js"></script>
    
</body>

</html>