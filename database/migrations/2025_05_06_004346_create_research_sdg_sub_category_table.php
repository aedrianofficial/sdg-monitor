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
        Schema::create('research_sdg_sub_category', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->uuid('research_id');
            $table->uuid('sdg_sub_category_id');
            $table->timestamps();

            $table->foreign('research_id')->references('id')->on('researches')->onDelete('cascade');
            $table->foreign('sdg_sub_category_id')->references('id')->on('sdg_sub_categories')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('research_sdg_sub_category');
    }
};
