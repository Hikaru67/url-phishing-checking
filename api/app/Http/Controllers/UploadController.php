<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class UploadController extends Controller
{
    /**
     * Upload file image
     *
     * @param Request $request
     * @return response
     */
    public function uploadImage(Request $request)
    {
        $request->validate([
            'file' => 'required|mimes:png,jpg|max:2048',
        ]);

        $path = config('app.cdn_url') . str_replace('public', '/storage', $request->file('file')->store('public/images/user-avatars'));
        
        return response()->json([
            'path' => $path
        ], 200);
    }

    /**
     * Delete image uploaded
     *
     * @param Request $request
     * @return Response
     */
    public function deleteImage(Request $request)
    {
        $request->validate([
            'filename' => 'required',
        ]);

        $path = 'public/images/user-avatars/' . $request->filename;
        if (Storage::exists($path)) {
            Storage::delete($path);

            return response()->json(['message' => 'Delete image successfully'], 200);
        }

        return response()->json(null, 204);
    }
}
