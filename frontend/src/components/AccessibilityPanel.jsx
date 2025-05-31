export default function AccessibilityPanel({ accessibility }) {
  return (
    <div className="bg-white rounded-2xl h-1/3 shadow p-4 overflow-auto">
      <h2 className="text-xl font-bold mb-4">Accessibility Updates</h2>
      {accessibility ? (
        <p className="text-gray-700 whitespace-pre-line">{accessibility}</p>
      ) : (
        <p className="text-gray-400 italic">No accessibility suggestions yet.</p>
      )}
    </div>
  );
}