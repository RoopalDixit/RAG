import React, { useState, useRef, useEffect } from 'react'
import axios from 'axios'
import './ChatInterface.css'

const API_BASE_URL = 'http://localhost:8000'

function ChatInterface({ chatHistory, setChatHistory, hasDocuments }) {
  const [question, setQuestion] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [chatHistory])

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!question.trim()) return
    if (!hasDocuments) {
      setError('Please upload at least one document before asking questions')
      return
    }

    setLoading(true)
    setError(null)

    // Store the question before clearing
    const currentQuestion = question.trim()
    setQuestion('')

    // Add user message to chat
    const userMessage = { human: currentQuestion, ai: '' }
    const updatedHistory = [...chatHistory, userMessage]
    setChatHistory(updatedHistory)

    try {
      // Format chat history for API (excluding the current message)
      const apiHistory = chatHistory.map(msg => ({
        human: msg.human,
        ai: msg.ai
      }))

      const response = await axios.post(`${API_BASE_URL}/ask`, {
        question: currentQuestion,
        chat_history: apiHistory
      })

      // Update chat with AI response
      userMessage.ai = response.data.answer

      // Add sources if available
      if (response.data.sources && response.data.sources.length > 0) {
        userMessage.sources = response.data.sources
      }
      
      setChatHistory([...chatHistory, userMessage])
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to get answer')
      // Remove the user message if there was an error and restore the question
      setQuestion(currentQuestion)
      setChatHistory(chatHistory)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="chat-interface">
      <div className="chat-messages">
        {chatHistory.length === 0 && (
          <div className="empty-state">
            <h2>👋 Welcome!</h2>
            <p>
              {hasDocuments
                ? 'Ask a question about your uploaded documents to get started.'
                : 'Upload a document first, then ask questions about it.'}
            </p>
          </div>
        )}

        {chatHistory.map((message, index) => (
          <div key={index} className="message-group">
            {message.human && (
              <div className="message user-message">
                <div className="message-header">You</div>
                <div className="message-content">{message.human}</div>
              </div>
            )}
            {message.ai && (
              <div className="message ai-message">
                <div className="message-header">Assistant</div>
                <div className="message-content">{message.ai}</div>
                {message.sources && message.sources.length > 0 && (
                  <div className="sources">
                    <strong>Sources:</strong>{' '}
                    {message.sources.join(', ')}
                  </div>
                )}
              </div>
            )}
          </div>
        ))}

        {loading && (
          <div className="message ai-message">
            <div className="message-header">Assistant</div>
            <div className="message-content">
              <div className="loading">Thinking...</div>
            </div>
          </div>
        )}

        {error && (
          <div className="error-message">
            ⚠️ {error}
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className="chat-input-form">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder={hasDocuments ? "Ask a question..." : "Upload a document first..."}
          disabled={loading || !hasDocuments}
          className="chat-input"
        />
        <button
          type="submit"
          disabled={loading || !hasDocuments || !question.trim()}
          className="send-button"
        >
          {loading ? '⏳' : '📤'}
        </button>
      </form>
    </div>
  )
}

export default ChatInterface
