import React, { useState } from 'react'
import DocumentUpload from './components/DocumentUpload'
import ChatInterface from './components/ChatInterface'
import './App.css'

function App() {
  const [uploadedDocuments, setUploadedDocuments] = useState([])
  const [chatHistory, setChatHistory] = useState([])

  const handleDocumentUpload = (filename) => {
    setUploadedDocuments(prev => [...prev, filename])
  }

  const handleClearDocuments = () => {
    setUploadedDocuments([])
    setChatHistory([])
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>📚 RAG Document Q&A System</h1>
        <p>Upload documents and ask questions powered by LangChain + ChromaDB</p>
      </header>

      <div className="app-container">
        <div className="sidebar">
          <DocumentUpload 
            onUpload={handleDocumentUpload}
            onClear={handleClearDocuments}
            uploadedDocuments={uploadedDocuments}
          />
        </div>

        <div className="main-content">
          <ChatInterface 
            chatHistory={chatHistory}
            setChatHistory={setChatHistory}
            hasDocuments={uploadedDocuments.length > 0}
          />
        </div>
      </div>
    </div>
  )
}

export default App
