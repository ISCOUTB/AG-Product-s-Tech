// Crear un objeto de rutas para cada sección
const rutas = {
    VolverLogin: './PRODUCTS-TECH/Frontend/Login/login.html',
    Regresar: './PRODUCTS-TECH/Frontend/VentanaUno/VentanaUno.html' 
};

// Función para manejar redirecciones
function redirigir(seccion) {
    window.location.href = rutas[seccion];
}

// Asociar eventos de click a cada botón
document.getElementById('btn-RegresarLogin').addEventListener('click', function() {
    redirigir('VolverLogin');
});
document.getElementById('Regresar').addEventListener('click', function() {
    redirigir('Regresar');
});
