<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Usuarios</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" >
</head>
<body>

<h1 class="display-5 mt-5 text-center text-primary">Consulta de Usuarios</h1>
<h3 class="display-5 mb-5 text-center text-danger">FastAPI</h3>

<div class="container">
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Nombre</th>
                <th scope="col">Edad</th>
                <th scope="col">Correo</th>
            </tr>
        </thead>
        <tbody>
            @foreach($usuarios as $usuario)
            <tr>
                <th scope="row">{{ $usuario['id'] }}</th>
                <td>{{ $usuario['name'] }}</td>
                <td>{{ $usuario['age'] }}</td>
                <td>{{ $usuario['email'] }}</td>
            </tr>
            <td>
    <a href="{{ route('usuario.edit', ['id' => $usuario['id']]) }}" class="btn btn-warning btn-sm">Editar</a>

    <form action="{{ route('usuario.destroy', ['id' => $usuario['id']]) }}" method="POST" style="display:inline;">
        @csrf
        @method('DELETE')
        <button type="submit" class="btn btn-danger btn-sm" onclick="return confirm('¿Estás seguro de eliminar este usuario?')">Eliminar</button>
    </form>
</td>

            @endforeach
        </tbody>
    </table>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" >
</script>
</body>
</html>
