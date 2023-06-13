
// Ver todos los eventos
const viewAllEventsButton = document.getElementById('viewAllEventsButton');
const responseContainerGetEvents = document.getElementById('responseContainerGetEvents');
const tableBody = document.getElementById('tableBody');

viewAllEventsButton.addEventListener('click', () => {
  fetch('http://localhost:8000/events')
    .then(response => response.json())
    .then(data => {
      if (data.length > 0) {
        generateTable(data);
      } else {
        responseContainerGetEvents.innerHTML = 'No hay eventos disponibles';
      }
    })
    .catch(error => {
      responseContainerGetEvents.innerHTML = 'Error al obtener los eventos';
    });
});

function generateTable(data) {
  tableBody.innerHTML = '';

  data.forEach(event => {
    const row = document.createElement('tr');

    for (const key in event) {
      const cell = document.createElement('td');
      cell.textContent = event[key];
      row.appendChild(cell);
    }

    tableBody.appendChild(row);
  });
}


// Ver un evento
//const viewEventButton = document.getElementById('viewEventButton');
//const responseContainerGetEvent = document.getElementById('responseContainerGetEvent');

//viewEventButton.addEventListener('click', () => {
//  const eventId = document.getElementById('eventId').value;

//  fetch(`http://localhost:8000/event/${eventId}`)
//    .then(response => response.json())
//    .then(data => {
//      responseContainerGetEvent.innerHTML = JSON.stringify(data, null, 2);
//    })
//    .catch(error => {
//      responseContainerGetEvent.innerHTML = 'Error al obtener los eventos';
//    });
//});

// Función para generar un ID único
function generateUniqueInteger() {
  const timestamp = new Date().getTime();
  const randomNum = Math.floor(Math.random() * 10000); // Generar un número aleatorio entre 0 y 9999
  const uniqueInteger = parseInt(`${timestamp}${randomNum}`, 10);
  
  return uniqueInteger;
}

// Agregar evento
const addEventButton = document.getElementById('addEventButton');
const responseContainerAddEvent = document.getElementById('responseContainerAddEvent');

addEventButton.addEventListener('click', () => {
  const eventName = document.getElementById('eventNameInput').value;
  const eventType = document.getElementById('eventTypeInput').value;
  const eventDate = document.getElementById('eventDateInput').value;
  const eventRecurrency = document.getElementById('eventRecurringInput').checked;

  const newEvent = {
    id: generateUniqueInteger(),
    name: eventName,
    type: eventType,
    date: eventDate,
    recurrency: eventRecurrency
  };

  if (Number.isInteger(generateUniqueInteger())) {
    fetch('http://localhost:8000/event/', {
      method: 'POST',
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newEvent)
    })
      .then(response => response.json())
      .then(data => {
        responseContainerAddEvent.innerHTML = JSON.stringify(data, null, 2);
      })
      .catch(error => {
        responseContainerAddEvent.innerHTML = 'Error al agregar el evento';
      });
  } else {
    alert('El ID del evento debe ser un número entero.');

    // Muestra un mensaje de error al usuario indicando que el valor ingresado no es válido
  }
});


// Eliminar un evento
const deleteEventButton = document.getElementById('deleteEventButton');
const responseContainerDeleteEvent = document.getElementById('responseContainerDeleteEvent');

deleteEventButton.addEventListener('click', () => {
  const deleteEventId = document.getElementById('deleteEventIdInput').value;

  fetch(`http://localhost:8000/event/${deleteEventId}`, {
    method: 'DELETE'
  })
  .then(response => response.json())
  then(data => {
    responseContainerDeleteEvent.innerHTML = JSON.stringify(data, null, 2);
  })
  .catch(error => {
    responseContainerDeleteEvent.innerHTML = 'Error al obtener los eventos';
  });
});