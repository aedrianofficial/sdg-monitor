<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class SdgSubCategory extends Model
{
    use HasFactory;

    public $incrementing = false;
    protected $keyType = 'string';

    protected $fillable = ['id', 'sdg_id', 'code', 'title', 'description'];

    protected static function boot()
    {
        parent::boot();
        static::creating(function ($model) {
            $model->id = (string) \Illuminate\Support\Str::uuid();
        });
    }

    public function sdg()
    {
        return $this->belongsTo(Sdg::class);
    }
    public function researches()
    {
        return $this->belongsToMany(Research::class, 'research_sdg_sub_category');
    }
}
