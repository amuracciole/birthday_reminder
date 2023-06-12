
// Ver todos los eventos
const viewAllEventsButton = document.getElementById('viewAllEventsButton');
const responseContainerGetEvents = document.getElementById('responseContainerGetEvents');

viewAllEventsButton.addEventListener('click', () => {
  fetch('http://localhost:8000/events')
    .then(response => response.json())
    .then(data => {
      responseContainerGetEvents.innerHTML = JSON.stringify(data, null, 2);
    })
    .catch(error => {
      responseContainerGetEvents.innerHTML = 'Error al obtener los eventos';
    });
});

// Ver un evento
const viewEventButton = document.getElementById('viewEventButton');
const responseContainerGetEvent = document.getElementById('responseContainerGetEvent');

viewEventButton.addEventListener('click', () => {
  const eventId = document.getElementById('eventId').value;

  fetch(`http://localhost:8000/event/${eventId}`)
    .then(response => response.json())
    .then(data => {
      responseContainerGetEvent.innerHTML = JSON.stringify(data, null, 2);
    })
    .catch(error => {
      responseContainerGetEvent.innerHTML = 'Error al obtener los eventos';
    });
});

// Agregar evento
const addEventButton = document.getElementById('addEventButton');
const responseContainerAddEvent = document.getElementById('responseContainerAddEvent');

addEventButton.addEventListener('click', () => {
  const eventId = parseInt(document.getElementById('eventIdInput').value);
  const eventName = document.getElementById('eventNameInput').value;
  const eventType = document.getElementById('eventTypeInput').value;
  const eventDate = document.getElementById('eventDateInput').value;
  const eventRecurrency = document.getElementById('eventRecurrencyInput').checked;

  const newEvent = {
    id: eventId,
    name: eventName,
    type: eventType,
    date: eventDate,
    recurrency: eventRecurrency
  };

  if (Number.isInteger(eventId)) {
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




