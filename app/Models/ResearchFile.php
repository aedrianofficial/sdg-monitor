<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class ResearchFile extends Model
{
    use HasFactory;

    public $incrementing = false;
    protected $keyType = 'string';

    protected $fillable = [
        'id',
        'research_id',
        'filename',
        'mime_type',
        'file_path',
    ];

    public function research()
    {
        return $this->belongsTo(Research::class);
    }
}
