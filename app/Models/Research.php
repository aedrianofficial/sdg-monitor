<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class Research extends Model
{
    use HasFactory;

    public $incrementing = false;
    protected $keyType = 'string';

    protected $fillable = [
        'id',
        'user_id',
        'research_status_id',
        'title',
        'abstract',
        'date_conducted',
        'is_active'
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function status()
    {
        return $this->belongsTo(ResearchStatus::class, 'research_status_id');
    }

    public function sdgs()
    {
        return $this->belongsToMany(Sdg::class, 'research_sdg');
    }

    public function sdgSubCategories()
    {
        return $this->belongsToMany(SdgSubCategory::class, 'research_sdg_sub_category');
    }

    public function files()
    {
        return $this->hasMany(ResearchFile::class);
    }
}
