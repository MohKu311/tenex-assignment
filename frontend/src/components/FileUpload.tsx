"use client";

import { useState } from "react";
import axios from "axios";
import LogCharts from "./LogCharts";

export default function FileUpload() {
  const [file, setFile] = useState<File | null>(null);
  const [uploadSuccess, setUploadSuccess] = useState(false);
  const [parsedData, setParsedData] = useState<any[]>([]);
  const [showOnlyAnomalies, setShowOnlyAnomalies] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = e.target.files?.[0];
    if (selected) setFile(selected);
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:5000/upload", formData);
      const { parsed } = res.data;

      setParsedData(parsed);
      setUploadSuccess(true);
    } catch (err) {
      console.error("Upload failed", err);
      setUploadSuccess(false);
    }
  };

  const filteredLogs = showOnlyAnomalies
    ? parsedData.filter((entry) => entry.anomaly)
    : parsedData;

  return (
    <div className="space-y-4">
      <div className="flex gap-4">
        <input type="file" onChange={handleFileChange} />
        <button
          onClick={handleUpload}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Upload
        </button>
      </div>

      {uploadSuccess && (
        <p className="text-green-700">✅ Upload successful</p>
      )}

      {parsedData.length > 0 && (
        <>
          <div className="flex items-center gap-4">
            <label className="flex items-center gap-2">
              <input
                type="checkbox"
                checked={showOnlyAnomalies}
                onChange={() => setShowOnlyAnomalies(!showOnlyAnomalies)}
              />
              Show only anomalies
            </label>
            <span className="text-sm text-gray-500">
              ({filteredLogs.length} shown out of {parsedData.length})
            </span>
          </div>

          <div>
            <h3 className="text-lg font-semibold mb-2">Parsed Logs:</h3>
            <div className="bg-gray-100 p-4 rounded shadow text-sm space-y-4">
              {filteredLogs.map((entry, idx) => (
                <div
                  key={idx}
                  className={`p-2 rounded ${
                    entry.anomaly
                      ? "bg-red-100 border border-red-400"
                      : "bg-white"
                  }`}
                >
                  <p>
                    <strong>Timestamp:</strong> {entry.timestamp}
                  </p>
                  <p>
                    <strong>Source IP:</strong> {entry.source_ip}
                  </p>
                  <p>
                    <strong>Destination IP:</strong> {entry.destination_ip}
                  </p>
                  <p>
                    <strong>URL:</strong> {entry.url}
                  </p>
                  <p>
                    <strong>Action:</strong> {entry.action}
                  </p>
                  <p>
                    <strong>Status Code:</strong> {entry.status_code}
                  </p>
                  <p>
                    <strong>User Agent:</strong> {entry.user_agent}
                  </p>
                  <p>
                    <strong>Threat Type:</strong> {entry.threat_type}
                  </p>
                  {entry.anomaly && (
                    <p className="text-red-600 font-bold">🚨 Anomaly Detected</p>
                  )}
                </div>
              ))}
            </div>
          </div>

          {/* 📊 Charts Section */}
          <LogCharts logs={filteredLogs} />
        </>
      )}
    </div>
  );
}
