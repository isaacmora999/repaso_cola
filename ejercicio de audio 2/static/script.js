function enviarPeticion() {
  fetch('/escuchar', {
    method: 'POST'
  })
  .then(res => res.json())
  .then(data => {
    const contenedor = document.getElementById('resultado');
    if (data.status === "ok") {
      contenedor.innerHTML = data.nombres.map(n => `<div class="nombre">${n}</div>`).join("");
    } else {
      alert(data.message);
    }
  })
  .catch(err => {
    console.error("❌ Error al conectar:", err);
    alert("Error de conexión con el servidor.");
  });
}
