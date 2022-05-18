<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Report extends Model
{
    use HasFactory;

    const TYPE = [
        'WHITE_LIST' => 0,
        'BLACK_LIST' => 1,
    ];

    protected $fillable = [
        'url',
        'type'
    ];

    public $selectable = [
        '*'
    ];
}
