// Crear un objeto de rutas para cada sección
const rutas = {
    proveedores: '/Users/PC/OneDrive/Documentos/LoginyVentana/Proovedores/Proovedores.html',  // Redirigir a VentanaDos.html por ahora
    inventario: '/Users/PC/OneDrive/Documentos/LoginyVentana/Inventario/Inventario.html',
    historial: '/Users/PC/OneDrive/Documentos/LoginyVentana/Historial/Historial.html',
    informes: '/Users/PC/OneDrive/Documentos/LoginyVentana/Informes/Informes.html',
    ventas: '/Users/PC/OneDrive/Documentos/LoginyVentana/Ventas/Ventas.html',
    compras: '/Users/PC/OneDrive/Documentos/LoginyVentana/Compras/Compras.html',
    VolverLogin: '/Users/PC/OneDrive/Documentos/LoginyVentana/Login/login.html'
};

// Función para manejar redirecciones
function redirigir(seccion) {
    window.location.href = rutas[seccion];
}

// Asociar eventos de click a cada botón
document.getElementById('btn-proveedores').addEventListener('click', function() {
    redirigir('proveedores');
});
document.getElementById('btn-inventario').addEventListener('click', function() {
    redirigir('inventario');
});
document.getElementById('btn-historial').addEventListener('click', function() {
    redirigir('historial');
});
document.getElementById('btn-informes').addEventListener('click', function() {
    redirigir('informes');
});
document.getElementById('btn-ventas').addEventListener('click', function() {
    redirigir('ventas');
});
document.getElementById('btn-compras').addEventListener('click', function() {
    redirigir('compras');
});
document.getElementById('btn-RegresarLogin').addEventListener('click', function() {
    redirigir('VolverLogin');
});

