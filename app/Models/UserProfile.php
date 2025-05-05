<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class UserProfile extends Model
{
    use HasFactory;

    public $incrementing = false; // Disable auto-increment
    protected $keyType = 'string'; // UUIDs are strings

    protected $fillable = [
        'id',
        'user_id',
        'first_name',
        'middle_initial',
        'last_name',
        'date_of_birth',
    ];

    // Automatically generate UUID when creating
    protected static function boot()
    {
        parent::boot();
        static::creating(function ($model) {
            $model->id = (string) \Illuminate\Support\Str::uuid();
        });
    }

    // Define relationship with the User model
    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
