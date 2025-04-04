from flask import Flask, request, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "supersecreto"

# Configuración básica
FASTAPI_URL = "http://localhost:5001"  

@app.route('/', methods=['GET'])
def home():
    return render_template('registro.html')

@app.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():
    try:
        usuario = {
            "name": request.form['txtNombre'],
            "age": int(request.form['txtEdad']),
            "email": request.form['txtCorreo']
        }
        response = requests.post(f"{FASTAPI_URL}/usuarios/", json=usuario)
        
        if response.status_code == 201:
            flash("Usuario guardado correctamente en FastAPI", "success")
        else:
            error_msg = response.json().get("mensaje", "Error al guardar")
            flash(f"Error: {error_msg}", "danger")

    except Exception as e:
        flash(f"Error de conexión: {str(e)}", "danger")

    return redirect(url_for('home'))

@app.route('/consultar_usuarios', methods=['GET'])
def consultar_usuarios():
    try:
        response = requests.get(f"{FASTAPI_URL}/usuarios")
        usuarios = response.json() if response.status_code == 200 else []
        return render_template('consulta.html', usuarios=usuarios)
    except Exception as e:
        flash(f"Error al obtener usuarios: {str(e)}", "danger")
        return render_template('consulta.html', usuarios=[])

@app.route('/editar_usuario/<int:id>', methods=['GET'])
def editar_usuario(id):
    try:
        response = requests.get(f"{FASTAPI_URL}/usuarios/{id}")
        
        if response.status_code == 200:
            usuario = response.json()
            return render_template('editar.html', usuario=usuario)
        else:
            flash("Usuario no encontrado", "danger")
            return redirect(url_for('consultar_usuarios'))
    except Exception as e:
        flash(f"Error al obtener usuario: {str(e)}", "danger")
        return redirect(url_for('consultar_usuarios'))

@app.route('/actualizar_usuario/<int:id>', methods=['POST'])
def actualizar_usuario(id):
    try:
        datos_actualizados = {
            "name": request.form['txtNombre'],
            "age": int(request.form['txtEdad']),
            "email": request.form['txtCorreo']
        }
        response = requests.put(f"{FASTAPI_URL}/usuarios/{id}", json=datos_actualizados)
        
        if response.status_code == 200:
            flash("Usuario actualizado correctamente", "success")
            return redirect(url_for('consultar_usuarios'))
        else:
            error_msg = response.json().get("mensaje", "Error al actualizar")
            flash(f"Error: {error_msg}", "danger")
            # Devolvemos al formulario de edición en caso de error
            response = requests.get(f"{FASTAPI_URL}/usuarios/{id}")
            if response.status_code == 200:
                usuario = response.json()
                return render_template('editar.html', usuario=usuario)
            else:
                return redirect(url_for('consultar_usuarios'))
    except Exception as e:
        flash(f"Error de conexión: {str(e)}", "danger")
        return redirect(url_for('consultar_usuarios'))

@app.route('/eliminar_usuario/<int:id>', methods=['GET'])
def eliminar_usuario(id):
    try:
        response = requests.delete(f"{FASTAPI_URL}/usuarios/{id}")
        
        if response.status_code == 200:
            flash("Usuario eliminado correctamente", "success")
        else:
            error_msg = response.json().get("mensaje", "Error al eliminar")
            flash(f"Error: {error_msg}", "danger")
    except Exception as e:
        flash(f"Error de conexión: {str(e)}", "danger")

    return redirect(url_for('consultar_usuarios'))

if __name__ == '__main__':    
    app.run(debug=True, port=8002)