<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

class ResearchStatusSeeder extends Seeder
{
    public function run(): void
    {
        $statuses = [
            'Proposed',
            'On-Going',
            'On-Hold',
            'Completed',
            'Declined',
        ];

        foreach ($statuses as $status) {
            DB::table('research_statuses')->insert([
                'id' => (string) Str::uuid(),
                'status' => $status,
                'created_at' => now(),
                'updated_at' => now(),
            ]);
        }
    }
}
