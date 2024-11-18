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

// Función para agregar una compra
function agregarCompra() {
    const producto = document.getElementById('productoCompra').value;
    const cantidad = document.getElementById('cantidadCompra').value;
    const precio = document.getElementById('precioCompra').value;

    fetch('http://127.0.0.1:8000/compras', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            producto: producto,
            cantidad: cantidad,
            precio: precio,
            fecha_compra: new Date().toISOString().split('T')[0] // Fecha actual
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Compra agregada:', data);
        cargarCompras(); // Recargar la lista de compras
        alert('Compra agregada exitosamente.');
        // Limpiar el formulario
        document.getElementById('productoCompra').value = '';
        document.getElementById('cantidadCompra').value = '';
        document.getElementById('precioCompra').value = '';
        document.getElementById('formCompra').style.display = 'none';
    })
    .catch(error => {
        console.error('Error al agregar la compra:', error);
        alert('Hubo un problema al agregar la compra. Inténtalo de nuevo.');
    });
}

// Función para eliminar una compra
function eliminarCompra(id_compra) {
    fetch(`http://127.0.0.1:8000/compras/{id_compra}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al eliminar la compra');
        }
        return response.json();
    })
    .then(data => {
        console.log('Compra eliminada:', data);
        cargarCompras(); // Recargar la lista de compras
        alert('Compra eliminada exitosamente.');
    })
    .catch(error => {
        console.error('Error al eliminar la compra:', error);
        alert('Hubo un problema al eliminar la compra. Inténtalo de nuevo.');
    });
}

// Función para cargar la lista de compras
function cargarCompras() {
    fetch('http://127.0.0.1:8000/compras')
    .then(response => response.json())
    .then(data => {
        const comprasList = document.getElementById('comprasList');
        comprasList.innerHTML = ''; // Limpiar lista actual

        data.forEach(compra => {
            const div = document.createElement('div');
            div.classList.add('compra-item');
            div.innerHTML = `
                <p><strong>Producto:</strong> ${compra.producto}</p>
                <p><strong>Cantidad:</strong> ${compra.cantidad}</p>
                <p><strong>Precio:</strong> $${compra.precio}</p>
                <p><em>Fecha de compra: ${compra.fecha_compra}</em></p>
                <button class="btnEliminarCompra" onclick="eliminarCompra(${compra.ID_compra})">Eliminar</button>
            `;
            comprasList.appendChild(div);
        });
    })
    .catch(error => {
        console.error('Error al cargar las compras:', error);
    });
}

// Función para mostrar el formulario para añadir una compra
document.getElementById('btnAñadir').addEventListener('click', function() {
    document.getElementById('formCompra').style.display = 'block';
});

// Botón para guardar la compra
document.getElementById('btnGuardarCompra').addEventListener('click', agregarCompra);

// Cargar la lista de compras al cargar la página
document.addEventListener('DOMContentLoaded', cargarCompras);