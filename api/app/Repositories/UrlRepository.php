<?php

namespace App\Repositories;

use App\Models\Url;
use DB;

class UrlRepository extends BaseRepository
{
    /**
     * @return  Url
     */
    public function getModel()
    {
        return Url::class;
    }

    /**
     * @param mixed $query
     * @param mixed $column
     * @param mixed $data
     *
     * @return Query
     */
    public function search($query, $column, $data)
    {
        switch ($column) {
            case 'url':
            case 'phone':
                return $query->where($column, 'like', '%' . $data . '%');
                break;
            case 'type':
                return $query->where($column, $data);
            default:
                return $query;
                break;
        }
    }

    public function filterUrl($url)
    {
        $parseUrl = parse_url($url);
        $result = '';
        if (isset($parseUrl['host']) && $parseUrl['host']) {
            $result = Url::where('url', 'like', '%www.' . $parseUrl['host'] . '%')
                ->orWhere('url', 'like', 'https://' . preg_replace('/^www\./', '', $parseUrl['host']) . '%')
                ->orWhere('url', 'like', 'http://' . preg_replace('/^www\./', '', $parseUrl['host']) . '%')
                ->orderBy('url')->first();
        }
        else {
            $result = Url::where('url', 'like', $url . '%')
                ->orWhere('url', 'like', 'https://' . $url . '%')
                ->orderBy('url')->first();
        }

        return $result;
    }
}