<?php
    $PERSONAL_KEY='some random character'
    $code=$_POST["code"];
	$body=$_POST["body"];
	if(strcmp($code,$PERSONAL_KEY)!=0)
            die('403');
	$fp = fopen('index.html', 'w');
	fwrite($fp, '<html>');
	fwrite($fp, '<head>');
	fwrite($fp, '<title>DeviantArtWatcher</title>');
	fwrite($fp, '</head>');
	fwrite($fp, '<body>');
	fwrite($fp, $body);
	fwrite($fp, '</body>');
	fwrite($fp, '</html>');
	fclose($fp);
        echo 'done';
?>
