<?php
$url = 'trtr/';
print(preg_match('/\/$/', $url));
if (preg_match('/\/$/', $url)) {
    // print($url);
    $urlsFilter = $url;
}