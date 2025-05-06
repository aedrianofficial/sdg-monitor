<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('research_files', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->uuid('research_id');
            $table->string('filename');
            $table->string('mime_type');
            $table->timestamps();

            $table->foreign('research_id')->references('id')->on('researches')->onDelete('cascade');
        });

        // Add LONGBLOB column for file content
        DB::statement("ALTER TABLE research_files ADD file_content LONGBLOB");
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('research_files');
    }
};
