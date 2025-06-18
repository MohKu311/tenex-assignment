import React, { useState } from 'react';
import axios from 'axios';

export default function FileUpload() {
  const [file, setFile] = useState<File | null>(null);
  const [parsedData, setParsedData] = useState<any[] | null>(null);
  const [status, setStatus] = useState<string>('');

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = e.target.files?.[0] || null;
    setFile(selected);
    setParsedData(null);
    setStatus('');
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    setStatus('Uploading...');

    try {
      const response = await axios.post('http://localhost:5000/upload', formData);
      setParsedData(response.data.parsed);
      setStatus('Upload successful');
    } catch (err) {
      setStatus('Upload failed');
      console.error(err);
    }
  };

  return (
    <div className="max-w-xl mx-auto p-6 space-y-4">
      <input
        type="file"
        accept=".log,.txt"
        onChange={handleFileChange}
        className="block w-full border rounded p-2"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Upload
      </button>

      {status && <p className="mt-2 text-sm text-gray-700">{status}</p>}

      {parsedData && (
        <div className="mt-6">
          <h2 className="font-semibold text-lg mb-2">Parsed Logs:</h2>
          <div className="bg-gray-100 rounded p-4 text-sm space-y-1">
            {parsedData.map((entry, idx) => (
              <div key={idx} className="flex gap-4">
                <span className="text-blue-600">{entry.timestamp}</span>
                <span>{entry.event}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
