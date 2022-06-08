<?php

namespace App\Http\Controllers;

use App\Models\Url;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Http;
use App\Repositories\UrlRepository;

class PhishingController extends Controller
{
    public function __construct(UrlRepository $urlRepository)
    {
        $this->urlRepository = $urlRepository;
    }

    public function urlPhishingChecking(Request $request)
    {
        $request->validate([
            'url' => 'required|regex:/^(http(s?):\/\/)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)/',
        ]);

        $url = $request->get('url');
        if (Cache::has($url)) {
            $cacheValue = Cache::get($url);

            return response()->json($cacheValue, 200);
        };
        $result = $this->urlRepository->filterUrl($url);

        if ($result) {
            $res = [
                'url' => $url,
                'label' => $result->type,
                'type' => 'success',
                'percent' => 98,
                'is_filtered' => 1,
                'features' => [],
                'suggestion' => $result->type ? 'bad' : 'good'
            ];
            Cache::put($url, $res, now()->addMinutes(10));

            return response()->json($res, 200);
        }

        $response = Http::post(config('app.url_machine_learning') . '/url-phishing-checking', [
            'url' => base64_encode($url)
        ]);

        $res = json_decode($response->body());
        Cache::put($url, $res, now()->addMinutes(10));

        return response()->json($res, 200);
    }
}
