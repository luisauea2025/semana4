let emprendimientos = [
    { id: 1, nombre: "BioAbono Orgánico", categoria: "Agricultura" },
    { id: 2, nombre: "App Delivery Local", categoria: "Tecnología" }
];

const formulario = document.getElementById('formulario');
const contenedorEmprendimientos = document.getElementById('contenedorEmprendimientos');
const mensajeExito = document.getElementById('mensajeExito');
const spinnerCarga = document.getElementById('spinnerCarga');

function renderizarEmprendimientos() {
    contenedorEmprendimientos.innerHTML = '';

    emprendimientos.forEach(emp => {
        const fila = document.createElement('tr');
        
        fila.innerHTML = `
            <td class="fw-bold">#${emp.id}</td>
            <td>${emp.nombre}</td>
            <td><span class="badge bg-secondary p-2">${emp.categoria}</span></td>
            <td class="text-center">
                <button class="btn btn-info btn-sm text-white me-1 fw-semibold" onclick="verDetalles(${emp.id})">
                    Ver Detalles
                </button>
                <button class="btn btn-danger btn-sm fw-semibold" onclick="eliminarEmprendimiento(${emp.id})">
                    Eliminar
                </button>
            </td>
        `;
        contenedorEmprendimientos.appendChild(fila);
    });
}

formulario.addEventListener('submit', function (event) {
    event.preventDefault();

    const idInput = document.getElementById('idEmprendimiento').value;
    const nombreInput = document.getElementById('nombre').value;
    const categoriaInput = document.getElementById('categoria').value;

    const existeId = emprendimientos.some(e => e.id == idInput);
    if (existeId) {
        alert("Error: El ID ingresado ya pertenece a un emprendimiento registrado.");
        return;
    }

    spinnerCarga.classList.remove('d-none');

    setTimeout(() => {
        emprendimientos.push({
            id: parseInt(idInput),
            nombre: nombreInput,
            categoria: categoriaInput
        });

        renderizarEmprendimientos();
        formulario.reset();

        spinnerCarga.classList.add('d-none');
        mensajeExito.classList.remove('d-none');

        setTimeout(() => {
            mensajeExito.classList.add('d-none');
        }, 3000);

    }, 1200);
});

function eliminarEmprendimiento(id) {
    emprendimientos = emprendimientos.filter(e => e.id !== id);
    renderizarEmprendimientos();
}

function verDetalles(id) {
    const emp = emprendimientos.find(e => e.id === id);
    if (emp) {
        document.getElementById('modalContenido').innerHTML = `
            <div class="p-2">
                <p><strong>Identificador Numérico:</strong> #${emp.id}</p>
                <p><strong>Nombre Comercial:</strong> ${emp.nombre}</p>
                <p><strong>Sector de Mercado:</strong> ${emp.categoria}</p>
                <hr>
                <p class="text-muted small mb-0">💡 Registro guardado en el almacenamiento temporal de la sesión del navegador de manera exitosa.</p>
            </div>
        `;

        const miModal = new bootstrap.Modal(document.getElementById('detalleModal'));
        miModal.show();
    }
}

document.addEventListener('DOMContentLoaded', renderizarEmprendimientos);