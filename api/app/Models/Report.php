<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Report extends Model
{
    use HasFactory;

    const LABEL = [
        'WHITE_LIST' => 0,
        'BLACK_LIST' => 1,
    ];

    const TYPE = [
        'GOOD' => 1,
        'BAD' => 2,
    ];

    protected $fillable = [
        'url',
        'label',
        'type',
        'user_id',
        'ip'
    ];

    public $selectable = [
        '*'
    ];
}
