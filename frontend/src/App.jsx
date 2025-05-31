import { useState } from 'react';
import UploadPanel from './components/UploadPanel';
import SummaryPanel from './components/SummaryPanel';
// import AccessibilityPanel from './components/AccessibilityPanel';

export default function Dashboard() {
  const [selectedOptions, setSelectedOptions] = useState({ summary: true, accessibility: true });
  const [summary, setSummary] = useState('');
  // const [accessibility, setAccessibility] = useState('');

  const handleFileUpload = (file) => {
    setSummary(file);
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 p-4 min-h-screen bg-gray-100">
      <UploadPanel
        onFileUpload={handleFileUpload}
        selectedOptions={selectedOptions}
        setSelectedOptions={setSelectedOptions}
      />
      <SummaryPanel summary={summary} />
    </div>
  );
}
