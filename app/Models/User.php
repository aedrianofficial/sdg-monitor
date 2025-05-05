<?php

namespace App\Models;

// use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use HasFactory, Notifiable;

    public $incrementing = false; // Important: disable auto-increment
    protected $keyType = 'string'; // UUIDs are strings

    protected $fillable = [
        'id',
        'email',
        'password',
    ];

    protected $hidden = [
        'password',
        'remember_token',
    ];

    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',
        ];
    }

    public function roles()
    {
        return $this->belongsToMany(Role::class, 'user_role');
    }

    // Automatically generate UUID when creating
    protected static function boot()
    {
        parent::boot();
        static::creating(function ($model) {
            $model->id = (string) \Illuminate\Support\Str::uuid();
        });
    }
}
// Note: The UUID generation is done in the model's boot method, which ensures that every time a new user is created, a unique UUID is generated and assigned to the 'id' field. This is crucial for maintaining the integrity of the database and ensuring that each user has a unique identifier.
