<?php

namespace App\Http\Controllers;

use App\Http\Resources\UrlResource;
use App\Models\Url;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Cache;

class UrlController extends Controller
{
    public function index(Request $request)
    {
        $type = $request->get('type');

        switch ($type) {
            case '0':
            case '1':
                if (Cache::has('url_' . $type)) {
                    $urls = Cache::get('url_' . $type);
                    return UrlResource::collection($urls);
                }
                $urls = Url::where('type', $type)->get();
                Cache::put('url_' . $type, $urls);

                break;

            default:
                $urls = Url::all();

                break;
        }

        return UrlResource::collection($urls);
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
