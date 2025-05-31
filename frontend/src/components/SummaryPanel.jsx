export default function SummaryPanel({ summary }) {
  // Filter available sections
  const sections = [
    summary.summary && {
      title: "Summary",
      content: <p className="whitespace-pre-line">{summary.summary}</p>
    },
    summary.important_points && summary.important_points.length > 0 && {
      title: "Important Points",
      content: (
        <ul className="list-disc list-inside space-y-1">
          {summary.important_points.map((point, idx) => (
            <li key={idx}>{point}</li>
          ))}
        </ul>
      ),
    },
    (summary.anecdotes && summary.anecdotes.length > 0) && {
      title: "Anecdotes",
      content: (
        <ul className="list-disc list-inside space-y-1">
          {summary.anecdotes.map((anecdote, idx) => (
            <li key={idx}>{anecdote}</li>
          ))}
        </ul>
      ),
    },
  ].filter(Boolean);

  return (
    <div className="h-full bg-white rounded-2xl shadow p-4 overflow-y-auto">
      <h1 className="text-xl font-bold mb-4 italic">Summary To Your File</h1>
      <div className="bg-white overflow-y-auto">
        <div className={`grid gap-6 h-full w-full`} style={{ gridTemplateRows: `repeat(${sections.length}, 1fr)` }}>
          {sections.map((section, idx) => (
            <div key={idx} className="p-6 overflow-auto">
              <h2 className="text-xl font-bold mb-4">{section.title}</h2>
              <div className="text-gray-800">{section.content}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
