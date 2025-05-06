<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class Sdg extends Model
{
    use HasFactory;

    public $incrementing = false;
    protected $keyType = 'string';

    protected $fillable = ['id', 'sdg_number', 'title', 'description'];

    protected static function boot()
    {
        parent::boot();
        static::creating(function ($model) {
            $model->id = (string) \Illuminate\Support\Str::uuid();
        });
    }

    public function images()
    {
        return $this->hasMany(SdgImg::class);
    }
    public function researches()
    {
        return $this->belongsToMany(Research::class, 'research_sdg');
    }
    public function subCategories()
    {
        return $this->hasMany(SdgSubCategory::class);
    }
}
