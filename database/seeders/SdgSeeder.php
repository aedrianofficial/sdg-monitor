<?php

namespace Database\Seeders;

use App\Models\Sdg;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Carbon;
use Illuminate\Support\Str;

class SdgSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run()
    {
        $sdgs = [
            [
                'sdg_number' => '01',
                'title' => 'No Poverty',
                'description' => 'End poverty in all its forms everywhere.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '02',
                'title' => 'Zero Hunger',
                'description' => 'End hunger, achieve food security and improved nutrition and promote sustainable agriculture.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '03',
                'title' => 'Good Health and Well-being',
                'description' => 'Ensure healthy lives and promote well-being for all at all ages.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '04',
                'title' => 'Quality Education',
                'description' => 'Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '05',
                'title' => 'Gender Equality',
                'description' => 'Achieve gender equality and empower all women and girls.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '06',
                'title' => 'Clean Water and Sanitation',
                'description' => 'Ensure availability and sustainable management of water and sanitation for all.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '07',
                'title' => 'Affordable and Clean Energy',
                'description' => 'Ensure access to affordable, reliable, sustainable and modern energy for all.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '08',
                'title' => 'Decent Work and Economic Growth',
                'description' => 'Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '09',
                'title' => 'Industry, Innovation and Infrastructure',
                'description' => 'Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '10',
                'title' => 'Reduced Inequalities',
                'description' => 'Reduce inequality within and among countries.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '11',
                'title' => 'Sustainable Cities and Communities',
                'description' => 'Make cities and human settlements inclusive, safe, resilient and sustainable.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '12',
                'title' => 'Responsible Consumption and Production',
                'description' => 'Ensure sustainable consumption and production patterns.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '13',
                'title' => 'Climate Action',
                'description' => 'Take urgent action to combat climate change and its impacts.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '14',
                'title' => 'Life Below Water',
                'description' => 'Conserve and sustainably use the oceans, seas and marine resources for sustainable development.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '15',
                'title' => 'Life on Land',
                'description' => 'Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and halt biodiversity loss.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '16',
                'title' => 'Peace, Justice and Strong Institutions',
                'description' => 'Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
            [
                'sdg_number' => '17',
                'title' => 'Partnerships for the Goals',
                'description' => 'Strengthen the means of implementation and revitalize the global partnership for sustainable development.',
                'created_at' => Carbon::now(),
                'updated_at' => Carbon::now(),
            ],
        ];
        foreach ($sdgs as $sdg) {
            Sdg::create([
                'id' => Str::uuid(),
                'sdg_number' => $sdg['sdg_number'],
                'title' => $sdg['title'],
                'description' => $sdg['description'],
            ]);
        }
    }

}
