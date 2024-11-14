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
    login: '/Users/PC/OneDrive/Documentos/LoginyVentana/VentanaUno/VentanaUno.html'  // Redirigir a VentanaDos.html por ahora
};

// Función para manejar redirecciones
function redirigir(seccion) {
    window.location.href = rutas[seccion];
}

/*
// Asociar eventos de click a cada botón
document.getElementById('iniciar-sesion-btn').addEventListener('click', function() {
    redirigir('login');
});
*/

//REGISTRO
// Esperar a que todo el DOM esté cargado antes de ejecutar el script
document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('container');
    const registerBtn = document.getElementById('register');
    const loginBtn = document.getElementById('login');

    // Manejar el registro
    registerBtn.addEventListener('click', () => {
        container.classList.add("active");
    });

    // Manejar el inicio de sesión
    loginBtn.addEventListener('click', () => {
        container.classList.remove("active");
    });

    // Manejar el inicio de sesión
    document.getElementById('iniciar-sesion-btn').addEventListener('click', function() {
        const email = document.querySelector('.sign-in input[type="email"]').value;
        const contrasena = document.querySelector('.sign-in input[type="password"]').value;

        if (email && contrasena) {
            // Obtener el arreglo de usuarios del localStorage
            const usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
            
            // Verificar si el usuario existe
            const usuarioEncontrado = usuarios.find(usuario => usuario.email === email && usuario.contrasena === contrasena);

            if (usuarioEncontrado) {
                // Guardar la información en sessionStorage
                sessionStorage.setItem('userEmail', usuarioEncontrado.email);
                sessionStorage.setItem('userName', usuarioEncontrado.nombreCompleto);

                // Redirigir a VentanaUno.html
                window.location.href = '/Users/PC/OneDrive/Documentos/LoginyVentana/VentanaUno/VentanaUno.html';
            } else {
                alert('Credenciales incorrectas. Por favor, intenta de nuevo.');
            }
        } else {
            alert('Por favor, completa los campos de inicio de sesión.');
        }
    });

    // Manejar el registro
    document.querySelector('.sign-up form').addEventListener('submit', function(e) {
        e.preventDefault(); // Evitar el envío del formulario

        const nombreCompleto = document.querySelector('.sign-up input[placeholder="Nombre Completo"]').value;
        const nombreUsuario = document.querySelector('.sign-up input[placeholder="Nombre de usuario"]').value;
        const email = document.querySelector('.sign-up input[type="email"]').value;
        const contrasena = document.querySelector('.sign-up input[type="password"]').value;

        // Verificar si todos los campos están completos
        if (nombreCompleto && nombreUsuario && email && contrasena) {
            agregarUsuario(nombreCompleto, nombreUsuario, email, contrasena);
            alert('Usuario registrado exitosamente.');
            
            // Opcional: Reiniciar el formulario o redirigir a otra página
            document.querySelector('.sign-up form').reset();
        } else {
            alert('Por favor, completa todos los campos.');
        }
    });

    // Función para agregar un nuevo usuario
    function agregarUsuario(nombreCompleto, nombreUsuario, email, contrasena) {
        // Obtener el arreglo de usuarios del localStorage
        let usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
        
        // Crear un nuevo usuario
        const nuevoUsuario = {
            nombreCompleto: nombreCompleto,
            nombreUsuario: nombreUsuario,
            email: email,
            contrasena: contrasena // Considera no guardar la contraseña en texto plano por razones de seguridad
        };

        // Agregar el nuevo usuario al arreglo
        usuarios.push(nuevoUsuario);
        
        // Guardar el arreglo actualizado en localStorage
        localStorage.setItem('usuarios', JSON.stringify(usuarios));
    }
});

// Asociar eventos de click a cada botón
document.getElementById('iniciar-sesion-btn').addEventListener('click', function() {
    redirigir('login');
});
