// Crear un objeto de rutas para cada sección
const rutas = {
    VolverLogin: '/Users/PC/OneDrive/Documentos/LoginyVentana/Login/login.html',
    Regresar: '/Users/PC/OneDrive/Documentos/LoginyVentana/VentanaUno/VentanaUno.html' 
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