import { useState } from 'react';
import axios from 'axios';

export default function UploadPanel({ onFileUpload, selectedOptions, setSelectedOptions }) {
  const [file, setFile] = useState(null);
  const [isSummarizing, setIsSummarizing] = useState(false);
  const [url, setUrl] = useState("");

  const handleUpload = async (e) => {
    if (!file) return;
    setIsSummarizing(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post('http://localhost:8000/summarize-file', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      onFileUpload(res.data.summary);
    } catch (err) {
      console.error('Upload failed', err);
    } finally {
      setIsSummarizing(false); // Stop loading
    }
  };

  const handleUrlSubmit = async (e) => {
    if (url == "") return;
    setIsSummarizing(true);
    const payload = {
      "url": url
    }
    const backendUrl = process.env.REACT_APP_BACKEND_URL;
    try {
      const res = await axios.post(`${backendUrl}/summarize-url`, payload, {
        headers: { 'Content-Type': 'application/json' },
      });
      onFileUpload(res.data.summary);
    } catch (err) {
      console.error('URL could not be parsed', err);
    } finally {
      setIsSummarizing(false);
    }
  };

  return (
    <div className="bg-white rounded-2xl shadow p-4 h-1/3">
      <h2 className="text-xl font-bold mb-4">Upload File</h2>
      <div className='flex justify-between items-center gap-4'>
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="mb-4"
        />

        <button
          onClick={handleUpload}
          disabled={isSummarizing}
          className={`px-4 py-2 rounded bg-blue-600 text-white font-semibold transition 
          ${isSummarizing ? 'opacity-50 cursor-not-allowed' : 'hover:bg-blue-700 cursor-pointer'}`}
        >
          {isSummarizing ? "Summarizing for You!" : "Upload and Summarize"}
        </button>
      </div>
      <div className="mt-6">
        <h2 className="text-xl font-bold mb-4">Summarize from URL</h2>
        <div className="flex justify-between gap-4">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter article or research paper URL"
            className="flex-1 max-w-md px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <button
            onClick={handleUrlSubmit}
            disabled={isSummarizing}
            className={`px-4 py-2 rounded bg-blue-600 text-white font-semibold transition
        ${isSummarizing
                ? 'bg-blue-400 cursor-not-allowed opacity-70'
                : 'bg-blue-600 hover:bg-blue-700 cursor-pointer'}
      `}
          >
            {isSummarizing ? "Summarizing for You!" : "Summarize URL"}
          </button>
        </div>
      </div>
    </div>
  );
}
