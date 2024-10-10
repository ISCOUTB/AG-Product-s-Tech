// Crear un objeto de rutas para cada sección
const rutas = {
    proveedores: './PRODUCTS-TECH/Frontend/Proovedores/Proovedores.html',  // Redirigir a VentanaDos.html por ahora
    inventario: './PRODUCTS-TECH/Frontend/Inventario/Inventario.html',
    historial: './PRODUCTS-TECH/Frontend/Historial/Historial.html',
    informes: './PRODUCTS-TECH/Frontend/Informes/Informes.html',
    ventas: './PRODUCTS-TECH/Frontend/Ventas/Ventas.html',
    compras: './PRODUCTS-TECH/Frontend/Compras/Compras.html',
    VolverLogin: './PRODUCTS-TECH/Frontend/Login/login.html'
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

