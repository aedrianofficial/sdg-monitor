<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;
class UserProfileSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $users = User::all();
        $profiles = [
            ['first_name' => 'Alice', 'last_name' => 'Cruz', 'date_of_birth' => '1995-05-10'],
            ['first_name' => 'Bob', 'last_name' => 'Smith', 'date_of_birth' => '1990-03-22'],
            ['first_name' => 'Carol', 'last_name' => 'Tan', 'date_of_birth' => '1988-11-02'],
            ['first_name' => 'Dave', 'last_name' => 'Reyes', 'date_of_birth' => '1992-07-14'],
        ];

        foreach ($users as $index => $user) {
            DB::table('user_profiles')->insert([
                'id' => Str::uuid(),
                'user_id' => $user->id,
                'first_name' => $profiles[$index]['first_name'],
                'last_name' => $profiles[$index]['last_name'],
                'date_of_birth' => $profiles[$index]['date_of_birth'],
                'created_at' => now(),
                'updated_at' => now(),
            ]);
        }
    }
}
