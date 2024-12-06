import React, { useState } from "react";
import ChatBox from "./components/Chatbox";  // Ensure correct import for ChatBox

const App = () => {
  const [message, setMessage] = useState("");  // User's current message
  const [messages, setMessages] = useState([]);  // Array of all messages
  const [loading, setLoading] = useState(false);  // Loading state for UI

  // Function to handle sending a message
  const handleSendMessage = async () => {
    if (message.trim() === "") return;  // Don't send if the message is empty

    setLoading(true);  // Set loading state while waiting for response

    // Create a new user message object
    const newMessage = {
      text: message,
      sender: "User",
    };

    // Update messages state to include the new message
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setMessage("");  // Clear the message input field

    try {
      // Send the message to the backend API
      const response = await fetch("http://127.0.0.1:8000/chat/send", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });

      // Get the response from the backend
      const data = await response.json();

      // Handle the response from the backend
      if (data.response) {
        // Create a bot message object
        const botMessage = {
          text: data.response,
          sender: "Assistant",
        };

        // Update messages state to include the bot's message
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      } else {
        // Handle case where no response was received
        const errorMessage = {
          text: "Error: Could not get a response from the server.",
          sender: "Assistant",
        };
        setMessages((prevMessages) => [...prevMessages, errorMessage]);
      }
    } catch (error) {
      // Handle any errors during the API request
      const errorMessage = {
        text: "Error: Unable to connect to the backend.",
        sender: "Assistant",
      };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setLoading(false);  // Set loading state to false after response is handled
    }
  };

  return (
    <div className="app">
      <ChatBox messages={messages} />  {/* Chatbox displaying all messages */}
      <div className="input-container">
        <input
          type="text"
          placeholder="Type a message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}  // Update message state as user types
        />
        <button onClick={handleSendMessage} disabled={loading}>
          {loading ? "Sending..." : "Send"}  {/* Button text changes when loading */}
        </button>
      </div>
    </div>
  );
};

export default App;


