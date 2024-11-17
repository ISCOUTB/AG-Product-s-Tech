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
  const btnAgregarEvento = document.getElementById("btnAgregarEvento");
  const eventoHistorial = document.getElementById("eventoHistorial");

  // Función para agregar un nuevo evento
  btnAgregarEvento.addEventListener("click", function() {
    const nuevoEvento = eventoHistorial.value;
    if (nuevoEvento.trim() === '') {
      alert('Por favor, ingrese un evento.');
      return;
    }

    fetch('http://127.0.0.1:8009/historial', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        evento: nuevoEvento,
        fecha: new Date().toISOString().split('T')[0], // Fecha actual
      }),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Evento agregado:', data);
      cargarHistorial(); // Recargar el historial
      eventoHistorial.value = ''; // Limpiar el campo de entrada
      alert('Evento agregado exitosamente.');
    })
    .catch(error => {
      console.error('Error al agregar el evento:', error);
      alert('Hubo un problema al agregar el evento. Inténtalo de nuevo.');
    });
  });

  // Función para eliminar todos los eventos
  deleteBtn.addEventListener("click", function() {
    fetch('http://127.0.0.1:8009/historial', {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Error al borrar los eventos');
      }
      return response.json();
    })
    .then(data => {
      console.log('Eventos eliminados:', data);
      cargarHistorial(); // Recargar el historial
      alert('Todos los eventos han sido eliminados.');
    })
    .catch(error => {
      console.error('Error al eliminar los eventos:', error);
      alert('Hubo un problema al borrar los eventos. Inténtalo de nuevo.');
    });
  });

  // Función para cargar el historial desde la API
  function cargarHistorial() {
    fetch('http://127.0.0.1:8009/historial')
    .then(response => response.json())
    .then(data => {
      historial.innerHTML = ''; // Limpiar la lista actual
      data.forEach(evento => {
        const li = document.createElement("li");
        li.textContent = `${evento.evento} - ${evento.fecha}`;
        historial.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error al cargar el historial:', error);
    });
  }

  // Cargar el historial al cargar la página
  cargarHistorial();
});
