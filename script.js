// Base de datos simulada en memoria (Semana 7)
let emprendimientos = [
    { id: 1, nombre: "BioAbono Orgánico", categoria: "Agricultura" },
    { id: 2, nombre: "App Delivery Local", categoria: "Tecnología" }
];

// Captura de elementos del DOM
const formulario = document.getElementById('formulario');
const contenedorEmprendimientos = document.getElementById('contenedorEmprendimientos');
const mensajeExito = document.getElementById('mensajeExito');
const spinnerCarga = document.getElementById('spinnerCarga');

// FUNCIÓN DE RENDERIZADO DINÁMICO (Semana 7 mejorada con clases de Bootstrap)
function renderizarEmprendimientos() {
    contenedorEmprendimientos.innerHTML = ''; // Limpiar la tabla antes de renderizar

    emprendimientos.forEach(emp => {
        const fila = document.createElement('tr');
        
        fila.innerHTML = `
            <td class="fw-bold">#${emp.id}</td>
            <td>${emp.nombre}</td>
            <td><span class="badge bg-secondary p-2">${emp.categoria}</span></td>
            <td class="text-center">
                <!-- Botón Info de Bootstrap que activa la función del Modal -->
                <button class="btn btn-info btn-sm text-white me-1 fw-semibold" onclick="verDetalles(${emp.id})">
                    Ver Detalles
                </button>
                <!-- Botón Danger de Bootstrap para eliminar -->
                <button class="btn btn-danger btn-sm fw-semibold" onclick="eliminarEmprendimiento(${emp.id})">
                    Eliminar
                </button>
            </td>
        `;
        contenedorEmprendimientos.appendChild(fila);
    });
}

// MANEJADOR DEL EVENTO SUBMIT (Semana 6 mejorado con Spinner y Alertas)
formulario.addEventListener('submit', function (event) {
    event.preventDefault(); // Evitar recarga de página

    // Captura de valores de los inputs
    const idInput = document.getElementById('idEmprendimiento').value;
    const nombreInput = document.getElementById('nombre').value;
    const categoriaInput = document.getElementById('categoria').value;

    // VALIDACIÓN DINÁMICA (Semana 6): Evitar IDs duplicados
    const existeId = emprendimientos.some(e => e.id == idInput);
    if (existeId) {
        alert("Error: El ID ingresado ya pertenece a un emprendimiento registrado.");
        return;
    }

    // ACTIVACIÓN DEL SPINNER (Quita la clase oculta de Bootstrap 'd-none')
    spinnerCarga.classList.remove('d-none');

    // Simulación de proceso de carga en red (Asíncrono simulado)
    setTimeout(() => {
        // Añadir nuevo registro al arreglo
        emprendimientos.push({
            id: parseInt(idInput),
            nombre: nombreInput,
            categoria: categoriaInput
        });

        // Actualizar la interfaz visual
        renderizarEmprendimientos();
        formulario.reset(); // Limpiar el formulario

        // APAGAR EL SPINNER
        spinnerCarga.classList.add('d-none');

        // MOSTRAR ALERTA DE ÉXITO BOOTSTRAP
        mensajeExito.classList.remove('d-none');

        // Temporizador de 3 segundos exactos para ocultar la alerta (Como se observa en tu captura)
        setTimeout(() => {
            mensajeExito.classList.add('d-none');
        }, 3000);

    }, 1200); // 1.2 segundos de retraso para apreciar la animación del Spinner
});

// FUNCIÓN DINÁMICA PARA ELIMINAR REGISTROS (Mantenida exactamente como tu captura)
function eliminarEmprendimiento(id) {
    // Filtrar el arreglo excluyendo el ID seleccionado
    emprendimientos = emprendimientos.filter(e => e.id !== id);
    // Volver a dibujar la tabla
    renderizarEmprendimientos();
}

// FUNCIÓN PARA RECOLECTAR DATOS Y DESPLEGAR EL MODAL BOOTSTRAP
function verDetalles(id) {
    const emp = emprendimientos.find(e => e.id === id);
    if (emp) {
        // Estructura limpia usando texto formateado dentro del modal
        document.getElementById('modalContenido').innerHTML = `
            <div class="p-2">
                <p><strong>Identificador Numérico:</strong> #${emp.id}</p>
                <p><strong>Nombre Comercial:</strong> ${emp.nombre}</p>
                <p><strong>Sector de Mercado:</strong> ${emp.categoria}</p>
                <hr>
                <p class="text-muted small mb-0">💡 Registro guardado en el almacenamiento temporal de la sesión del navegador de manera exitosa.</p>
            </div>
        `;

        // Instanciar y disparar la ventana modal nativa de Bootstrap
        const miModal = new bootstrap.Modal(document.getElementById('detalleModal'));
        miModal.show();
    }
}

// RENDERIZADO INICIAL AL CARGAR COMPLETAMENTE EL DOM (Mantenida exactamente como tu captura)
document.addEventListener('DOMContentLoaded', renderizarEmprendimientos);