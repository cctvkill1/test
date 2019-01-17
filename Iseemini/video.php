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
    <link rel="stylesheet" href="css/sti_style.css" type="text/css" media="screen">
</head>
<style>
    body{
        background: #000;
    }
    .title{
        font-size: 28px;
        color: #fff;
        padding: 50px 40px;
    }
    video{
        width: 100%;
    }
</style>
<body> 
    <video src="movies/<?php echo $movie['m3u8'];?>" controls="controls"  poster="image/<?php echo $movie['img'];?>">
        您的浏览器不支持 video 标签。
    </video>
</body>

</html>