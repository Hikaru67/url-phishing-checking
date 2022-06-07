<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::post('/url-phishing-checking', 'PhishingController@urlPhishingChecking');
Route::get('urls', 'UrlController@index');
Route::post('/report', 'UrlController@store');
Route::get('/clear-cache', function () {
    Cache::flush();
});
