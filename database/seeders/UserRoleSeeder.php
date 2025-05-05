<?php
namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\User;
use App\Models\Role;

class UserRoleSeeder extends Seeder
{
    public function run(): void
    {
        $users = User::all();
        $roles = Role::all()->pluck('id', 'role'); // [role => id]

        $users[0]->roles()->attach($roles['contributor']);
        $users[1]->roles()->attach($roles['reviewer']);
        $users[2]->roles()->attach($roles['approver']);
        $users[3]->roles()->attach($roles['admin']);
    }
}
// This seeder will attach the roles to the users based on their index.
