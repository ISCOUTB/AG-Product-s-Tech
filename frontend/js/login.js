document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('container');
    const registerBtn = document.getElementById('go-register');
    const loginBtn = document.getElementById('login');

    registerBtn.addEventListener('click', () => {
        container.classList.add("active");
    });

    loginBtn.addEventListener('click', () => {
        container.classList.remove("active");
    });

    // Crear un objeto de rutas para cada sección
    const rutas = {
        login: 'VentanaUno/VentanaUno.html'  // Redirigir a VentanaDos.html por ahora
    };

    // Función para manejar redirecciones
    function redirigir(seccion) {
        window.location.href = rutas[seccion];
    }

    // Asociar eventos de click a cada botón
    const iniciarBtn = document.getElementById('iniciar-sesion-btn');
    if (iniciarBtn) {
        iniciarBtn.addEventListener('click', function() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const data = {
                email: email,
                password: password
            };

            fetch('http://127.0.0.1:8000/login/', {
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
                console.log('Inicio de sesión exitoso:', data);
                alert('Inicio de sesión exitoso');
                // Redirige al usuario a otra página
                window.location.href = 'menu.html';
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al iniciar sesión: ' + error.message);
            });
        });
    }
});