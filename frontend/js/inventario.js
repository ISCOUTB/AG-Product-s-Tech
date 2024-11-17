// Crear un objeto de rutas para cada sección
const rutas = {
    VolverLogin: 'Login/login.html',
    Regresar: 'VentanaUno/VentanaUno.html'
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


//Para el carrusel que despues me confundo
const leftArrow = document.getElementById('leftArrow');
const rightArrow = document.getElementById('rightArrow');
const carouselImages = document.querySelector('.carousel-images');
const totalImages = carouselImages.children.length;
let imageIndex = 0;
const visibleImages = 5;  // Número de imágenes visibles
const imageWidth = 220;   // Ancho de cada imagen (210px de ancho + 5px de margen a cada lado)

// Actualizar el estado de los botones
function updateArrows() {
    leftArrow.disabled = imageIndex === 0;
    rightArrow.disabled = imageIndex >= totalImages - visibleImages;
}

rightArrow.addEventListener('click', () => {
    if (imageIndex < totalImages - visibleImages) {
        imageIndex++;
        carouselImages.style.transform = `translateX(-${imageWidth * imageIndex}px)`;
    }
    updateArrows();
});

leftArrow.addEventListener('click', () => {
    if (imageIndex > 0) {
        imageIndex--;
        carouselImages.style.transform = `translateX(-${imageWidth * imageIndex}px)`;
    }
    updateArrows();
});

// Al cargar la página, actualizar los botones
updateArrows();

// Obtener los elementos
const btnLogin = document.getElementById('btn-AbrirUsuario');
const btnParticipants = document.getElementById('btn-InfoAutores');
const loginDropdown = document.getElementById('loginDropdown');
const participantsDropdown = document.getElementById('participantsDropdown');

// Función para alternar visibilidad del dropdown
function toggleDropdown(dropdown) {
    dropdown.classList.toggle('show');
}

// Asociar los eventos de clic a los botones
btnLogin.addEventListener('click', (event) => {
    event.stopPropagation();  // Evitar que el evento se propague
    toggleDropdown(loginDropdown);
    participantsDropdown.classList.remove('show'); // Cerrar el otro dropdown si está abierto
});

btnParticipants.addEventListener('click', (event) => {
    event.stopPropagation();
    toggleDropdown(participantsDropdown);
    loginDropdown.classList.remove('show');
});

// Cerrar dropdowns al hacer clic fuera de ellos
window.addEventListener('click', () => {
    loginDropdown.classList.remove('show');
    participantsDropdown.classList.remove('show');
});

//LHECHEOVIEFPIVHHFRVPHRPHTBHPTHPTHPBHTPTBPHPBPHTPONHPTYP5NHP5YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
window.onload = function() {
    let currentImageItem;  // Variable para almacenar el elemento actualmente seleccionado en el carrusel
    let proveedores = [];  // Lista para almacenar proveedores dinámicamente

    const btnMostrarForm = document.getElementById('btnMostrarForm');
    const formAgregar = document.getElementById('formAgregar');
    const cerrarForm = document.getElementById('cerrarForm');
    const btnAgregarImagen = document.getElementById('btnAgregarImagen');
    const btnBuscarProveedor = document.getElementById('btnBuscarProveedor');
    const busquedaProveedor = document.getElementById('busquedaProveedor');
    const cerrarBusqueda = document.getElementById('cerrarBusqueda');
    const inputBusqueda = document.getElementById('inputBusqueda');
    const listaResultados = document.getElementById('listaResultados');

    if (btnMostrarForm && formAgregar) {
        btnMostrarForm.addEventListener('click', function() {
            formAgregar.style.display = 'block';
        });
    }

    if (cerrarForm) {
        cerrarForm.addEventListener('click', function() {
            formAgregar.style.display = 'none';
        });
    }

    if (btnAgregarImagen) {
        btnAgregarImagen.addEventListener('click', function() {
            const imagenInput = document.getElementById('inputImagen');
            const tituloInput = document.getElementById('inputTitulo').value;
            const descripcionInput = document.getElementById('inputDescripcion').value;

            if (imagenInput.files && imagenInput.files[0]) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const nuevoItem = document.createElement('div');
                    nuevoItem.classList.add('item');
                    nuevoItem.setAttribute('data-titulo', tituloInput);
                    nuevoItem.setAttribute('data-descripcion', descripcionInput);

                    nuevoItem.innerHTML = `<img src="${e.target.result}" alt="${tituloInput}">`;

                    document.getElementById('carouselImages').appendChild(nuevoItem);
                    formAgregar.style.display = 'none'; // Cerrar automáticamente el formulario

                    // Asignar evento de clic a la nueva imagen para mostrar detalles
                    nuevoItem.addEventListener('click', function() {
                        mostrarDetallesImagen(nuevoItem);
                    });

                    // Actualizar lista de proveedores para la búsqueda
                    actualizarListaProveedores();

                    // Actualizar el estado del carrusel después de agregar la nueva imagen
                    updateArrows();
                };
                reader.readAsDataURL(imagenInput.files[0]);
            } else {
                alert("Por favor seleccione una imagen.");
            }
        });
    }

    // Función para mostrar detalles de la imagen seleccionada
    function mostrarDetallesImagen(item) {
        const titulo = item.getAttribute('data-titulo');
        const descripcion = item.getAttribute('data-descripcion');
        const imagenSrc = item.querySelector('img').src;

        document.getElementById('detalleImagenSrc').src = imagenSrc;
        document.getElementById('detalleTitulo').textContent = titulo;
        document.getElementById('detalleDescripcion').textContent = descripcion;
        document.getElementById('detalleImagen').style.display = 'block';

        // Guardamos el elemento actual para poder eliminarlo
        currentImageItem = item;
    }

    // Cerrar el modal de detalles
    const cerrarDetalles = document.getElementById('cerrarDetalles');
    if (cerrarDetalles) {
        cerrarDetalles.addEventListener('click', function() {
            document.getElementById('detalleImagen').style.display = 'none';
        });
    }

    // Función para eliminar la imagen y su información del carrusel
    const btnEliminarImagen = document.getElementById('btnEliminarImagen');
    if (btnEliminarImagen) {
        btnEliminarImagen.addEventListener('click', function() {
            if (currentImageItem) {
                currentImageItem.remove();  // Eliminar el elemento del DOM
                document.getElementById('detalleImagen').style.display = 'none'; // Cerrar el modal de detalles
                updateArrows();  // Actualizar las flechas del carrusel
                actualizarListaProveedores(); // Actualizar la lista de proveedores
            }
        });
    }

    // Asignar eventos a las imágenes iniciales del carrusel
    function asignarEventosAImagenesIniciales() {
        const imagenes = document.querySelectorAll('.carousel-images .item');
        imagenes.forEach(function(item) {
            item.addEventListener('click', function() {
                mostrarDetallesImagen(item);
            });
        });
    }

    asignarEventosAImagenesIniciales();

    // Mostrar cuadro de búsqueda si el botón de búsqueda existe
    if (btnBuscarProveedor && busquedaProveedor) {
        btnBuscarProveedor.addEventListener('click', function() {
            busquedaProveedor.style.display = 'block';
        });

        cerrarBusqueda.addEventListener('click', function() {
            busquedaProveedor.style.display = 'none';
        });
    }

    // Vincular el evento input a la función filtrarProveedores
    if (inputBusqueda) {
        inputBusqueda.addEventListener('input', filtrarProveedores);
    }

    // Función para filtrar proveedores por nombre
    function filtrarProveedores() {
        const filtro = inputBusqueda.value.toLowerCase();
        const resultados = proveedores.filter(function(proveedor) {
            return proveedor.titulo.toLowerCase().includes(filtro);
        });

        // Mostrar los resultados en la lista
        listaResultados.innerHTML = ''; // Limpiar la lista anterior
        resultados.forEach(function(proveedor) {
            const li = document.createElement('li');
            li.textContent = proveedor.titulo;
            li.addEventListener('click', function() {
                // Desplazar el carrusel a la posición del proveedor seleccionado
                irACarrusel(proveedor.index);
                busquedaProveedor.style.display = 'none'; // Cerrar el cuadro de búsqueda
            });
            listaResultados.appendChild(li);
        });
    }

    // Función para ir a una posición específica del carrusel
    function irACarrusel(index) {
        const carouselImages = document.querySelector('.carousel-images');
        const offset = -(220 * index); // Cambia 220 por el ancho de tus imágenes
        carouselImages.style.transform = `translateX(${offset}px)`;
        imageIndex = index;
        updateArrows();
    }

    // Función para actualizar la lista de proveedores (títulos e índices)
    function actualizarListaProveedores() {
        const imagenes = document.querySelectorAll('.carousel-images .item');
        proveedores = []; // Limpiar la lista
        imagenes.forEach(function(item, index) {
            const titulo = item.getAttribute('data-titulo');
            proveedores.push({ titulo: titulo, index: index });
        });
        filtrarProveedores(); // Llamar a la función para actualizar los resultados de búsqueda en tiempo real
    }

    actualizarListaProveedores(); // Actualizar lista al cargar la página

    // Código del carrusel restaurado y mejorado
    const leftArrow = document.getElementById('leftArrow');
    const rightArrow = document.getElementById('rightArrow');
    const carouselImages = document.querySelector('.carousel-images');
    let imageIndex = 0;
    const visibleImages = 5;
    const imageWidth = 220; 

    function updateArrows() {
        const totalImages = carouselImages.children.length;
        leftArrow.disabled = imageIndex === 0;
        rightArrow.disabled = imageIndex >= totalImages - visibleImages;
    }

    rightArrow.addEventListener('click', () => {
        const totalImages = carouselImages.children.length;
        if (imageIndex < totalImages - visibleImages) {
            imageIndex++;
            const offset = -(imageWidth * imageIndex);
            carouselImages.style.transform = `translateX(${offset}px)`;
        }
        updateArrows();
    });

    leftArrow.addEventListener('click', () => {
        if (imageIndex > 0) {
            imageIndex--;
            const offset = -(imageWidth * imageIndex);
            carouselImages.style.transform = `translateX(${offset}px)`;
        }
        updateArrows();
    });

    updateArrows(); // Al cargar la página, actualizar el estado de las flechas
};
const btnMostrarForm = document.getElementById('btnMostrarForm');
const btnbusform = document.getElementById('btnbusForm');
const btnactuform = document.getElementById('btnactForm');
const btnform = document.getElementById('btnForm');

if (btnMostrarForm && formagregar) {
    btnMostrarForm.addEventListener('click', function() {
        formagregar.style.display = 'block';
    });
}
if (btnForm && formeliminar) {
    btnForm.addEventListener('click', function() {
        formeliminar.style.display = 'block';
    });
}
if (btnForm && formeliminar) {
    btnForm.addEventListener('click', function() {
        formeliminar.style.display = 'block';
    });
}
if (btnForm && formeliminar) {
    btnForm.addEventListener('click', function() {
        formeliminar.style.display = 'block';
    });
}

fetch('/productos/btneliminar{id_producto}', {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        titulo: titulo,
        descripcion: descripcion,
        imagen: imagenSrc,
    }),
})
.then(response => {
    if (!response.ok) {
        throw new Error('Error al eliminar la imagen en el servidor');
    }
    return response.json();
})
.then(data => {
    console.log('Imagen eliminada en el servidor:', data);

    // Eliminar la imagen del DOM
    currentImageItem.remove();
    document.getElementById('detalleImagen').style.display = 'none'; // Cerrar el modal de detalles
    updateArrows();
    actualizarListaProveedores();
})
.catch(error => {
    console.error('Error al procesar la solicitud:', error);
    alert('Hubo un problema al eliminar la imagen. Inténtalo de nuevo.');
});

fetch('/productos/btnbuscar{id_producto}', {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        titulo: titulo,
        descripcion: descripcion,
        imagen: imagenSrc,
    }),
})
.then(response => {
    if (!response.ok) {
        throw new Error('Error al eliminar la imagen en el servidor');
    }
    return response.json();
})
.then(data => {
    console.log('Imagen eliminada en el servidor:', data);

    // Eliminar la imagen del DOM
    currentImageItem.remove();
    document.getElementById('detalleImagen').style.display = 'none'; // Cerrar el modal de detalles
    updateArrows();
    actualizarListaProveedores();
})
.catch(error => {
    console.error('Error al procesar la solicitud:', error);
    alert('Hubo un problema al eliminar la imagen. Inténtalo de nuevo.');
});

fetch('/productos/btnactualizar{id_producto}', {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        titulo: titulo,
        descripcion: descripcion,
        imagen: imagenSrc,
    }),
})
.then(response => {
    if (!response.ok) {
        throw new Error('Error al eliminar la imagen en el servidor');
    }
    return response.json();
})
.then(data => {
    console.log('Imagen eliminada en el servidor:', data);

    // Eliminar la imagen del DOM
    currentImageItem.remove();
    document.getElementById('detalleImagen').style.display = 'none'; // Cerrar el modal de detalles
    updateArrows();
    actualizarListaProveedores();
})
.catch(error => {
    console.error('Error al procesar la solicitud:', error);
    alert('Hubo un problema al eliminar la imagen. Inténtalo de nuevo.');
});

fetch('/productos/btnagregar{id_producto}', {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        titulo: titulo,
        descripcion: descripcion,
        imagen: imagenSrc,
    }),
})
.then(response => {
    if (!response.ok) {
        throw new Error('Error al eliminar la imagen en el servidor');
    }
    return response.json();
})
.then(data => {
    console.log('Imagen eliminada en el servidor:', data);

    // Eliminar la imagen del DOM
    currentImageItem.remove();
    document.getElementById('detalleImagen').style.display = 'none'; // Cerrar el modal de detalles
    updateArrows();
    actualizarListaProveedores();
})
.catch(error => {
    console.error('Error al procesar la solicitud:', error);
    alert('Hubo un problema al eliminar la imagen. Inténtalo de nuevo.');
});
