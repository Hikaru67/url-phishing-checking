<?php

namespace App\Http\Controllers;

use App\Models\Url;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class PhishingController extends Controller
{
    public function urlPhishingChecking(Request $request)
    {
        $request->validate([
            'url' => 'required|regex:/^(http(s?):\/\/)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)/',
        ]);

        $url = $request->get('url');
        $parseUrl = parse_url($url);
        $result = '';
        if (isset($parseUrl['host']) && $parseUrl['host']) {
            $result = Url::where('url',  $parseUrl['host'])->first();
            if (!$result) {
                $result = Url::where('url', 'www.' . $parseUrl['host'] . '%')
                    ->orWhere('url', 'like', '%www.' . $parseUrl['host'] . '%')
                    ->orWhere('url', 'like', 'https://' . preg_replace('/^www\./', '', $parseUrl['host']) . '%')
                    ->orWhere('url', 'like', '%www.' . $parseUrl['host'] . '%')
                    ->orderBy('url')->first();
            }
            if (!$result) {
                $result = Url::where('url', 'like', '%www.' . $parseUrl['host'] . '%')->first();
            }
        }
        if (!$result) {
            $result = Url::where('url', 'like', $url . '%')->first();
            if ($result && !preg_match('/^(http|https)/u', $url)) {
                $url = 'https://' + $url;
                $result = Url::where('url', 'like', $url . '%')->first();
            }
        }

        if ($result ) {
            return response()->json([
                'label' => $result->type ? 'bad' : 'good',
                'type' => 'success',
                'percent' => 86,
                'features' => []
            ], 200);
        }

        $response = Http::post(config('app.url_machine_learning') . '/get_phishing_url', [
            'url' => base64_encode($url)
        ]);

        return json_decode($response->body());
    }
}
