
<?php 
$visitor_number = intval(file_get_contents('visitor_number.txt')) + 1;
$movies = json_decode(file_get_contents('movies.json'), true);

file_put_contents('visitor_number.txt', $visitor_number);
?>

<!DOCTYPE HTML>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <title>田聪的私人影院</title>
    <link rel="stylesheet" href="css/sti_style.css" type="text/css" media="screen">
</head>

<body>

    <div class="sti_container">

        <div class="slider_description"> 田聪的私人影院 </div>

        <div class="sti_slider">  
                <div class="sti_slide">
                    <?php 
                    foreach ($movies as $key => $value) {
                        if (0 == $key % 2) {
                            ?>
                    <div class="sti_shelf_divider"></div>
                    <?php
                        } ?>
                    <a href="video.php?id=<?php echo $key; ?>" class="sti_prod">
                        <img src="image/<?php echo $value['img']; ?>" alt="" width="110" height="150">
                        <img class="fx_shadow" src="img/fx_shadow.png" style="height: 150px;">
                        <img class="fx_leftside" src="img/fx_leftside.png" style="height: 150px;"> 
                        <?php 
                        if ($key < 2) {
                            ?>
                        <i class="ribbon ribbon_red" title="Ribbon"></i>
                    <?php
                        } ?> 
                    </a>
                    <?php
                    }
                    ?> 
                    <div class="sti_shelf_divider_bottom"></div>
                </div>
 
            <p class='visitor'>总访客人数：<?php echo $visitor_number; ?></p>
        </div>

    </div>
</body>

</html> 