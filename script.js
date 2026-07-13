// ==========================================
// 1. SELECCIÓN DE ELEMENTOS DEL DOM
// ==========================================
const formulario = document.getElementById('formulario-registro');
const inputNombre = document.getElementById('nombre');
const inputDescripcion = document.getElementById('descripcion');
const selectCategoria = document.getElementById('categoria');
const alerta = document.getElementById('mensaje-alerta');
const contenedorRegistros = document.getElementById('contenedor-registros');
const contadorTotal = document.getElementById('contador-total');

// Variable global para controlar el total de registros
let totalRegistros = 0;

// 2. Función para actualizar el contador en pantalla
function actualizarContador() {
    contadorTotal.textContent = totalRegistros;
}

// ==========================================
// NUEVO: FUNCIONES REUTILIZABLES DE VALIDACIÓN
// ==========================================

// Valida el campo Nombre (Obligatorio y longitud mínima de 3 caracteres)
function validarNombre() {
    const valor = inputNombre.value.trim();
    if (valor === '') {
        inputNombre.classList.add('is-invalid');
        inputNombre.classList.remove('is-valid');
        return false;
    } else if (valor.length < 3) {
        inputNombre.classList.add('is-invalid');
        inputNombre.classList.remove('is-valid');
        return false;
    } else {
        inputNombre.classList.add('is-valid');
        inputNombre.classList.remove('is-invalid');
        return true;
    }
}

// Valida la Descripción (Obligatorio e información suficiente: mínimo 10 caracteres)
function validarDescripcion() {
    const valor = inputDescripcion.value.trim();
    if (valor === '') {
        inputDescripcion.classList.add('is-invalid');
        inputDescripcion.classList.remove('is-valid');
        return false;
    } else if (valor.length < 10) {
        inputDescripcion.classList.add('is-invalid');
        inputDescripcion.classList.remove('is-valid');
        return false;
    } else {
        inputDescripcion.classList.add('is-valid');
        inputDescripcion.classList.remove('is-invalid');
        return true;
    }
}

// Valida que el usuario seleccione una categoría
function validarCategoria() {
    const valor = selectCategoria.value;
    if (valor === '') {
        selectCategoria.classList.add('is-invalid');
        selectCategoria.classList.remove('is-valid');
        return false;
    } else {
        selectCategoria.classList.add('is-valid');
        selectCategoria.classList.remove('is-invalid');
        return true;
    }
}

// ==========================================
// NUEVO: EVENTOS EN TIEMPO REAL (input y blur)
// ==========================================
// Validan mientras el usuario escribe ('input') o cuando sale del campo ('blur')
inputNombre.addEventListener('input', validarNombre);
inputNombre.addEventListener('blur', validarNombre);

inputDescripcion.addEventListener('input', validarDescripcion);
inputDescripcion.addEventListener('blur', validarDescripcion);

selectCategoria.addEventListener('change', validarCategoria);
selectCategoria.addEventListener('blur', validarCategoria);


// ==========================================
// 3. CAPTURA DEL EVENTO 'SUBMIT'
// ==========================================
formulario.addEventListener('submit', function (event) {
    // Evita que la página se recargue por defecto
    event.preventDefault();

    // Ejecutamos las validaciones obligatorias antes de registrar
    const nombreValido = validarNombre();
    const descripcionValida = validarDescripcion();
    const categoriaValida = validarCategoria();

    // Permite registrar información ÚNICAMENTE si todas las validaciones son correctas (true)
    if (nombreValido && descripcionValida && categoriaValida) {
        
        // Si todo está bien, ocultamos y limpiamos cualquier alerta de error previa
        alerta.classList.add('d-none');
        alerta.classList.remove('alert-danger');

        // Obtener los valores limpios
        const nombre = inputNombre.value.trim();
        const descripcion = inputDescripcion.value.trim();
        const categoria = selectCategoria.value;

        // 5. Creación de elementos HTML dinámicos usando createElement (Tu código original)
        const columnaCard = document.createElement('div');
        columnaCard.className = 'col-12 mb-3'; // Añadido un pequeño margen abajo

        const tarjeta = document.createElement('div');
        tarjeta.className = 'card h-100 border-start border-primary border-4 shadow-sm';

        const cuerpoTarjeta = document.createElement('div');
        cuerpoTarjeta.className = 'card-body d-flex justify-content-between align-items-start';

        const infoContenedor = document.createElement('div');

        const titulo = document.createElement('h5');
        titulo.className = 'card-title mb-1 fw-bold';
        titulo.textContent = nombre;

        const insignia = document.createElement('span');
        insignia.className = 'badge bg-info text-dark mb-2';
        insignia.textContent = categoria;

        const textoDescripcion = document.createElement('p');
        textoDescripcion.className = 'card-text text-muted small mb-0';
        textoDescripcion.textContent = descripcion;

        // Botón para eliminar el registro individual
        const botonEliminar = document.createElement('button');
        botonEliminar.className = 'btn btn-outline-danger btn-sm';
        botonEliminar.innerHTML = 'Eliminar'; 

        // 6. Manejo del evento click en el botón Eliminar
        botonEliminar.addEventListener('click', function () {
            columnaCard.remove(); 
            totalRegistros--;     
            actualizarContador(); 
        });

        // 7. Estructurar los elementos mediante appendChild
        infoContenedor.appendChild(titulo);
        infoContenedor.appendChild(insignia);
        infoContenedor.appendChild(textoDescripcion);

        cuerpoTarjeta.appendChild(infoContenedor);
        cuerpoTarjeta.appendChild(botonEliminar);

        tarjeta.appendChild(cuerpoTarjeta);
        columnaCard.appendChild(tarjeta);

        // Insertar la tarjeta completa en el contenedor principal del HTML
        contenedorRegistros.appendChild(columnaCard);

        // 8. Incrementar y actualizar el contador global
        totalRegistros++;
        actualizarContador();

        // MOSTRAR MENSAJE DINÁMICO DE ÉXITO CON CLASES BOOTSTRAP
        alerta.textContent = '¡Registro completado con éxito!';
        alerta.className = 'alert alert-success mt-3'; // Aplica el color verde
        alerta.classList.remove('d-none');

        // 9. Limpiar el formulario para un nuevo registro
        formulario.reset();

        // Quitar los bordes verdes para que el formulario quede limpio para el siguiente uso
        inputNombre.classList.remove('is-valid');
        inputDescripcion.classList.remove('is-valid');
        selectCategoria.classList.remove('is-valid');

    } else {
        // MOSTRAR MENSAJE DINÁMICO DE ERROR CON CLASES BOOTSTRAP
        alerta.textContent = 'Por favor, completa todos los campos correctamente con la información solicitada.';
        alerta.className = 'alert alert-danger mt-3'; // Aplica el color rojo
        alerta.classList.remove('d-none');
    }
});