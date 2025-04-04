<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Usuario</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<form action="{{ route('usuario.update', ['id' => $usuario['id']]) }}" method="POST">
    @csrf
    @method('PUT')

    <h1 class="display-1 mt-5 text-center text-warning">Editar Usuario</h1>
    <h3 class="display-3 mb-5 text-center text-danger">FastAPI</h3>

    <div class="container">

        @if(session('success'))
            <div class="alert alert-success">{{ session('success') }}</div>
        @endif

        @if(session('error'))
            <div class="alert alert-danger">{{ session('error') }}</div>
        @endif

        <p class="text-center">
            <a href="{{ route('usuario.index') }}"> Volver a la Lista</a>
        </p>

        <div class="mb-3">
            <label class="form-label">Nombre:</label>
            <input type="text" name="txtNombre" class="form-control" value="{{ $usuario['name'] }}">
        </div>

        <div class="mb-3">
            <label class="form-label">Edad:</label>
            <input type="number" name="txtEdad" class="form-control" value="{{ $usuario['age'] }}">
        </div>

        <div class="mb-3">
            <label class="form-label">Correo:</label>
            <input type="email" name="txtCorreo" class="form-control" value="{{ $usuario['email'] }}">
        </div>

        <button type="submit" class="btn btn-warning">Actualizar</button>

    </div>
</form>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
