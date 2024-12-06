import React from "react";

// ChatBox component to display the messages
const ChatBox = ({ messages }) => {
  return (
    <div className="chatbox">
      {messages.map((msg, index) => (
        <div key={index} className={`message ${msg.sender}`}>
          <span>{msg.text}</span>
        </div>
      ))}
    </div>
  );
};

export default ChatBox;
