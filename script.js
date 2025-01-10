// script.js
document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent page reload

    const userInput = document.getElementById('user-input').value;
    const responseDiv = document.getElementById('response');

    // Show the user's query in the response area
    responseDiv.innerHTML = `<p><strong>You asked:</strong> ${userInput}</p><p>Loading response...</p>`;

    // Send the user input to the backend API
    fetch('http://127.0.0.1:8000/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: userInput })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Check if the response has a 'response' field
        if (data && data.response) {
            responseDiv.innerHTML = `<p><strong>Bot:</strong> ${data.response}</p>`;
        } else {
            responseDiv.innerHTML = `<p>Sorry, I couldn't process your request. Please try again.</p>`;
        }
    })
    .catch(error => {
        console.error('There was an error with the fetch operation:', error);
        responseDiv.innerHTML = `<p>Sorry, there was an error. Please try again later.</p>`;
    });
});
