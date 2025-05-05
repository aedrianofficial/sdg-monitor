<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $users = [
            ['email' => 'contributor@gmail.com'],
            ['email' => 'reviewer@gmail.com'],
            ['email' => 'approver@gmail.com'],
            ['email' => 'admin@gmail.com'],
        ];

        foreach ($users as $index => $userData) {
            User::create([
                'id' => Str::uuid(),
                'email' => $userData['email'],
                'password' => Hash::make('password'), // default password
            ]);
        }
    }
}
