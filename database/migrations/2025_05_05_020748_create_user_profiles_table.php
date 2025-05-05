<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('user_profiles', function (Blueprint $table) {
            $table->uuid('id')->primary(); // UUID as the primary key
            $table->uuid('user_id'); // Foreign key to users table
            $table->string('first_name');
            $table->string('middle_initial', 1)->nullable(); // Middle initial (nullable)
            $table->string('last_name');
            $table->date('date_of_birth');
            $table->timestamps();

            // Foreign key to ensure user_id references the id in users table
            $table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('user_profiles');
    }
};
