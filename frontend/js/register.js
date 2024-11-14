document.addEventListener('DOMContentLoaded', function() {
    const registerBtn = document.getElementById('register');

    registerBtn.addEventListener('click', function() {
        const fullName = document.querySelector('.sign-up input[placeholder="Nombre Completo"]').value;
        const username = document.querySelector('.sign-up input[placeholder="Nombre de usuario"]').value;
        const email = document.querySelector('.sign-up input[placeholder="Email"]').value;
        const password = document.querySelector('.sign-up input[placeholder="Contraseña"]').value;

        const data = {
            full_name: fullName,
            username: username,
            email: email,
            password: password
        };

        fetch('http://127.0.0.1:8009/register/', {
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
            console.error('Error:', error);
            alert('Error al registrar: ' + error.message);
        });
    });
});