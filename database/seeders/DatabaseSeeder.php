<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Str;
use Illuminate\Support\Facades\Hash;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
   // database/seeders/DatabaseSeeder.php

public function run(): void
{
    $this->call([
        RoleSeeder::class,
        UserSeeder::class,
        UserProfileSeeder::class,
        UserRoleSeeder::class,
    ]);
}

}
