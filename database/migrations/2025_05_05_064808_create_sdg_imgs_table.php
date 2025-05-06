<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void {
        Schema::create('sdg_imgs', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->uuid('sdg_id');
            $table->string('image_path');
            $table->timestamps();

            $table->foreign('sdg_id')->references('id')->on('sdgs')->onDelete('cascade');
        });
    }

    public function down(): void {
        Schema::dropIfExists('sdg_imgs');
    }
};
