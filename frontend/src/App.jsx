
import React, { useState, useRef, useEffect, useCallback, useMemo } from "react";
import "./App.css";
import StarsCanvas from "./StarsCanvas";

function App() {
  const [messages, setMessages] = useState([
    { id: 1, text: "Hi! Ask me anything about your data and I'll generate SQL queries for you.", sender: "bot" },
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const chatBoxRef = useRef(null);
  const messageIdRef = useRef(2);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    if (chatBoxRef.current) {
      chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
    }
  }, [messages]);

  // Optimized message adding function
  const addMessage = useCallback((text, sender) => {
    const newMessage = {
      id: messageIdRef.current++,
      text,
      sender,
      timestamp: new Date().toISOString()
    };
    setMessages(prev => [...prev, newMessage]);
    return newMessage.id;
  }, []);

  // Handle form submission with better error handling
  const handleSubmit = useCallback(async (e) => {
    e.preventDefault();
    const question = input.trim();
    if (!question || isLoading) return;

    // Add user message immediately
    addMessage(question, "user");
    setInput("");
    setIsLoading(true);
    
    // Add thinking message
    const thinkingId = addMessage("🤔 Analyzing your question...", "bot");

    try {
      const res = await fetch("http://127.0.0.1:8000/generate-sql/", {
        method: "POST",
        headers: { 
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ question }),
      });

      if (!res.ok) {
        throw new Error(`HTTP ${res.status}: ${res.statusText}`);
      }

      const data = await res.json();
      
      // Remove thinking message and add response
      setMessages(prev => prev.filter(msg => msg.id !== thinkingId));
      
      if (data.sql_query) {
        addMessage(
          `<div class="sql-response">
            <div class="sql-label">🔍 Generated SQL Query:</div>
            <div class="sql-code">${data.sql_query}</div>
            <div class="sql-tip">💡 You can copy this query to run in your database</div>
          </div>`,
          "bot"
        );
      } else {
        addMessage(`<span style='color:#ffb3b3'>❌ No SQL query generated. Please try rephrasing your question.</span>`, "bot");
      }
    } catch (err) {
      // Remove thinking message and show error
      setMessages(prev => prev.filter(msg => msg.id !== thinkingId));
      addMessage(
        `<div class="error-response">
          <div class="error-label">❌ Connection Error</div>
          <div class="error-text">${err.message}</div>
          <div class="error-tip">Make sure the backend server is running on port 8000</div>
        </div>`,
        "bot"
      );
    } finally {
      setIsLoading(false);
    }
  }, [input, isLoading, addMessage]);

  // Sample questions for better UX
  const sampleQuestions = useMemo(() => [
    "Show me all devices that are offline",
    "What's the average CPU usage across all servers?",
    "List all POS devices with high temperature",
    "Show network switches with high latency"
  ], []);

  const handleSampleClick = useCallback((question) => {
    setInput(question);
  }, []);

  return (
    <div className="App">
      <StarsCanvas />
      <div className="container">
        <h1>✨ SQL CHAT ✨</h1>
        <div className="chat-box" ref={chatBoxRef}>
          {messages.map((msg) => (
            <div className={`message ${msg.sender}`} key={msg.id}>
              <div
                className={msg.sender}
                dangerouslySetInnerHTML={{ __html: msg.text }}
              ></div>
            </div>
          ))}
        </div>
        
        {/* Sample questions for better UX */}
        {messages.length === 1 && (
          <div className="sample-questions">
            <div className="sample-label">💡 Try asking:</div>
            {sampleQuestions.map((question, idx) => (
              <button
                key={idx}
                className="sample-btn"
                onClick={() => handleSampleClick(question)}
                type="button"
              >
                {question}
              </button>
            ))}
          </div>
        )}

        <form onSubmit={handleSubmit} className="chat-form">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask a question about your data..."
            autoComplete="off"
            disabled={isLoading}
            required
          />
          <button type="submit" disabled={isLoading || !input.trim()}>
            {isLoading ? "🤔" : "Send"}
          </button>
        </form>
        <div className="footer">
          Made By Nithyashree iyer 
        </div>
      </div>
    </div>
  );
}

export default App;
