import MessageBubble from "./MessageBubble";

export default function ChatWindow({ messages }) {

  return (
    <div className="chat-window">

      {messages.map((msg, index) => (

        <MessageBubble
          key={index}
          role={msg.role}
          text={msg.text}
        />

      ))}

    </div>
  );
}