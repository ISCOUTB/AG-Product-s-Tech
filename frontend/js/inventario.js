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
