<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plant Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f7fc;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        h1 {
            text-align: center;
            color: #2C3E50;
        }
        #chatbox {
            border: 1px solid #ddd;
            padding: 10px;
            height: 300px;
            overflow-y: auto;
            margin-bottom: 20px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .message {
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .user-message {
            background-color: #3498db;
            color: white;
            text-align: right;
        }
        .bot-message {
            background-color: #ecf0f1;
            color: #34495e;
        }
        input[type="text"] {
            width: calc(100% - 20px);
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        button {
            padding: 10px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
            width: 100%;
        }
        button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Plant Chatbot</h1>
        <div id="chatbox"></div>
        <input type="text" id="user_input" placeholder="Ask about plants...">
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        const chatbox = document.getElementById('chatbox');
        const user_input = document.getElementById('user_input');

        function sendMessage() {
            const userMessage = user_input.value.trim();
            if (userMessage === "") return;
            
            // Display user message
            chatbox.innerHTML += `<div class="message user-message">${userMessage}</div>`;
            user_input.value = "";
            chatbox.scrollTop = chatbox.scrollHeight;

            // Send user message to FastAPI backend
            fetch('http://127.0.0.1:8000/chatbot', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                const botResponse = data.response;
                chatbox.innerHTML += `<div class="message bot-message">${botResponse}</div>`;
                chatbox.scrollTop = chatbox.scrollHeight;
            })
            .catch(error => {
                console.error('Error:', error);
                chatbox.innerHTML += `<div class="message bot-message">Sorry, something went wrong.</div>`;
                chatbox.scrollTop = chatbox.scrollHeight;
            });
        }
    </script>
</body>
</html>
