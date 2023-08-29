document.getElementById('lab5').addEventListener('submit', function(event) {
    event.preventDefault(); // Se pone para que no se recargue la página luego de apretar Calcular ya que previene el comportamiento por default, que es ese
    
    // Se obtienen los valores que se ingresaron en las casillas usando el id
    let nombre = document.getElementById('nombre').value;
    let peso = parseFloat(document.getElementById('peso').value);
    let altura = parseFloat(document.getElementById('altura').value);
    let edad = parseInt(document.getElementById('edad').value); // No se usan estos datos pero se obtienen correctamente
    let genero = document.getElementById('genero').value; // Lo mismo de arriba
    let actividad = document.getElementById('actividad').value;
    console.log(nombre,peso,altura,edad,genero,actividad); // Revisar si se obtienen correctamente
    
    // Calculo del IMC, (altura por altura es igual a altura al cuadrado)
    let imc = peso / (altura * altura);
  
    // Clasificación del usuario según el peso
    let clasificacion;
    if (imc > 0 && imc < 18.5) {
      clasificacion = 'Bajo peso';
    } else if (imc < 25) {
      clasificacion = 'Peso normal';
    } else if (imc < 30) {
      clasificacion = 'Sobrepeso';
    } else {
      clasificacion = 'Obesidad';
    }
    
    // Clasificación sde la actividad física
    let actividadFisica;  
    if (actividad === 'sedentario') {
        actividadFisica = 1.2;
      } else if (actividad === 'moderado') {
        actividadFisica = 1.55;
      } else if (actividad === 'activo') {
        actividadFisica = 1.9;
      }
      
    // Gasto Energético Diario (GED)
    let ged = actividadFisica * peso;
   
    // El Estado Nutricional
    let estadoNutricional;
    if (imc >= 18.5 && imc < 25) {
      estadoNutricional = 'Estado nutricional adecuado';
    } else {
      estadoNutricional = 'Necesita atención especializada';
    }
        // Se modifican elementos de HTML según los datos que se recibieron del usuario
        document.getElementById('nombreResultado').textContent = `Resultados para ${nombre}`;
        document.getElementById('imc').textContent = `IMC: ${imc.toFixed(2)}`; // Se redondea el número a 2 decimales
        document.getElementById('clasificacion').textContent = `Clasificación del IMC: ${clasificacion}`;
        document.getElementById('ged').textContent = `Gasto Energético Diario: ${ged.toFixed(2)} kcal`; // Se redondea también
        document.getElementById('estado').textContent = `Estado nutricional: ${estadoNutricional}`;
        document.getElementById('resultado').style.display = 'block'; // Se cambia el display a block para que se muestre (se le puede poner flex también pero se ve horrible)
  });
  