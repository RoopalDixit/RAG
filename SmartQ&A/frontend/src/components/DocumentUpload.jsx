import React, { useState } from 'react'
import axios from 'axios'
import './DocumentUpload.css'

const API_BASE_URL = 'http://localhost:8000'

function DocumentUpload({ onUpload, onClear, uploadedDocuments }) {
  const [uploading, setUploading] = useState(false)
  const [error, setError] = useState(null)
  const [success, setSuccess] = useState(null)

  const handleFileUpload = async (event) => {
    const file = event.target.files[0]
    if (!file) return

    setUploading(true)
    setError(null)
    setSuccess(null)

    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await axios.post(`${API_BASE_URL}/upload`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })

      setSuccess(`Document "${file.name}" uploaded successfully! ${response.data.chunks} chunks created.`)
      onUpload(file.name)
      
      // Clear success message after 3 seconds
      setTimeout(() => setSuccess(null), 3000)
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to upload document')
    } finally {
      setUploading(false)
    }
  }

  const handleClear = async () => {
    if (!window.confirm('Are you sure you want to clear all documents?')) {
      return
    }

    try {
      await axios.delete(`${API_BASE_URL}/clear`)
      onClear()
      setSuccess('All documents cleared successfully!')
      setTimeout(() => setSuccess(null), 3000)
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to clear documents')
    }
  }

  return (
    <div className="document-upload">
      <div className="upload-section">
        <h2>📄 Documents</h2>
        
        <div className="upload-area">
          <input
            type="file"
            id="file-upload"
            accept=".pdf,.txt,.docx,.csv,.md"
            onChange={handleFileUpload}
            disabled={uploading}
            style={{ display: 'none' }}
          />
          <label htmlFor="file-upload" className="upload-button">
            {uploading ? 'Uploading...' : '📤 Upload Document'}
          </label>
          <p className="upload-hint">
            Supported: PDF, TXT, DOCX, CSV, MD
          </p>
        </div>

        {error && (
          <div className="message error">
            ⚠️ {error}
          </div>
        )}

        {success && (
          <div className="message success">
            ✅ {success}
          </div>
        )}

        {uploadedDocuments.length > 0 && (
          <div className="uploaded-documents">
            <h3>Uploaded Documents ({uploadedDocuments.length})</h3>
            <ul>
              {uploadedDocuments.map((doc, index) => (
                <li key={index}>📄 {doc}</li>
              ))}
            </ul>
            <button onClick={handleClear} className="clear-button">
              🗑️ Clear All
            </button>
          </div>
        )}
      </div>
    </div>
  )
}

export default DocumentUpload
