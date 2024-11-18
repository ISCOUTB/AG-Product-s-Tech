document.addEventListener('DOMContentLoaded', function() {
    const registerBtn = document.getElementById('register');

    registerBtn.addEventListener('click', function() {
        const fullName = document.querySelector('.sign-up input[placeholder="Nombre Completo"]').value.trim();
        const username = document.querySelector('.sign-up input[placeholder="Nombre de usuario"]').value.trim();
        const email = document.querySelector('.sign-up input[placeholder="Email"]').value.trim();
        const password = document.querySelector('.sign-up input[placeholder="Contraseña"]').value.trim();
    
        if (!fullName || !username || !email || !password) {
            alert('Por favor, complete todos los campos.');
            return;
        }
    
        const data = {
            nombre_completo: fullName,
            nick: username,
            email: email,
            contrasena: password
        };

        fetch('http://127.0.0.1:8000/usuarios/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(error => { throw new Error(error.detail); });
            }
            return response.json();
        })
        .then(data => {
            console.log('Registro exitoso:', data);
            alert('Registro exitoso');
            // Redirige al usuario a otra página
            window.location.href = 'menu.html';
        })
        .catch(error => {
            console.error('Error completo:', JSON.stringify(error));
            alert('Error al registrar: ' + JSON.stringify(error));
        });
    });
});