document.addEventListener("DOMContentLoaded", function () {
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
  document.getElementById('btn-regresar').addEventListener('click', function() {
    redirigir('VolverLogin');
  });
  document.getElementById('Regresar').addEventListener('click', function() {
    redirigir('Regresar');
  });

  const historial = document.getElementById("historial");
  const deleteBtn = document.querySelector(".delete-btn");

  // Simulación de eventos
  const eventos = [
    'Compra de Laptop - 01/09/2024',
    'Compra de Monitor - 05/09/2024',
    'Compra de Teclado - 12/09/2024',
    'Compra de Mouse - 15/09/2024',
    'Compra de Audífonos - 18/09/2024'
  ];

  // Agrega los eventos al historial
  eventos.forEach(evento => {
    const li = document.createElement("li");
    li.textContent = evento;
    historial.appendChild(li);
  });

  // Función para borrar todos los eventos
  deleteBtn.addEventListener("click", function() {
    historial.innerHTML = ''; // Borra todos los elementos de la lista
  });
});
