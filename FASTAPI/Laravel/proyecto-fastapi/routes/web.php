<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;

Route::get('/', [UserController::class, 'inicio'])->name('usuario.inicio');
Route::post('/addUser', [UserController::class, 'store'])->name('usuario.store');
Route::get('/usuarios', [UserController::class, 'index'])->name('usuario.index');
Route::get('/usuarios/{id}/editar', [UserController::class, 'edit'])->name('usuario.edit');
Route::put('/usuarios/{id}', [UserController::class, 'update'])->name('usuario.update');
Route::delete('/usuarios/{id}', [UserController::class, 'destroy'])->name('usuario.destroy');
