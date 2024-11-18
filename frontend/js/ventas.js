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
document.getElementById('Regresar').addEventListener('click', function() {
    redirigir('Regresar');
});

// Elementos del DOM
const ventaDescripcion = document.getElementById('ventaDescripcion');
const btnAgregarVentaForm = document.getElementById('btnAgregarVentaForm');
const btnActualizar = document.getElementById('btnActualizar');
const btnEliminarVenta = document.getElementById('btnEliminarVenta');

// Función para agregar una venta
btnAgregarVentaForm.addEventListener('click', function() {
    const descripcion = ventaDescripcion.value;
    if (!descripcion.trim()) {
        alert('Por favor, ingrese una descripción para la venta.');
        return;
    }

    fetch('http://127.0.0.1:8000/ventas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            descripcion: descripcion,
            fecha: new Date().toISOString().split('T')[0], // Fecha actual
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Venta agregada:', data);
        alert('Venta agregada exitosamente.');
        cargarVentas(); // Recargar las ventas
        ventaDescripcion.value = ''; // Limpiar el campo de entrada
    })
    .catch(error => {
        console.error('Error al agregar la venta:', error);
        alert('Hubo un problema al agregar la venta. Inténtalo de nuevo.');
    });
});

// Función para eliminar todas las ventas
btnEliminarVenta.addEventListener('click', function() {
    fetch('http://127.0.0.1:8000/ventas', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al eliminar las ventas');
        }
        return response.json();
    })
    .then(data => {
        console.log('Ventas eliminadas:', data);
        alert('Todas las ventas han sido eliminadas.');
        cargarVentas(); // Recargar las ventas
    })
    .catch(error => {
        console.error('Error al eliminar las ventas:', error);
        alert('Hubo un problema al eliminar las ventas. Inténtalo de nuevo.');
    });
});

// Función para cargar las ventas desde la API
function cargarVentas() {
    fetch('http://127.0.0.1:8000/ventas')
    .then(response => response.json())
    .then(data => {
        const ventasList = document.getElementById('ventasList');
        ventasList.innerHTML = ''; // Limpiar la lista actual

        data.forEach(venta => {
            const li = document.createElement('li');
            li.textContent = `${venta.descripcion} - ${venta.fecha}`;
            ventasList.appendChild(li);
        });
    })
    .catch(error => {
        console.error('Error al cargar las ventas:', error);
    });
}

// Cargar las ventas al cargar la página
cargarVentas();
});