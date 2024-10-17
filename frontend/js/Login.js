/*
// Esperar a que todo el DOM esté cargado antes de ejecutar el script
document.addEventListener('DOMContentLoaded', function() {
    // Capturar el evento del botón de inicio de sesión
    var iniciarBtn = document.getElementById('iniciar-sesion-btn');
    
    if (iniciarBtn) {
        iniciarBtn.addEventListener('click', function() {
            // Redirigir a VentanaUno.html
            window.location.href = 'VentanaUno.html';
        });
    }
});
*/

const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
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
document.getElementById('iniciar-sesion-btn').addEventListener('click', function() {
    redirigir('login');
});
