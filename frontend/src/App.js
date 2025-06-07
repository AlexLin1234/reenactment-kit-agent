import { useState } from 'react';

function App() {
  const [century, setCentury] = useState('');
  const [region, setRegion] = useState('');
  const [role, setRole] = useState('');
  const [result, setResult] = useState(null);

  const runPipeline = async () => {
    const resp = await fetch('/api/pipeline', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ century, region, role })
    });
    const data = await resp.json();
    setResult(data);
  };

  const downloadZip = async () => {
    if (!result) return;
    const resp = await fetch('/api/references_zip', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ references: result.references })
    });
    const blob = await resp.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'references.zip';
    a.click();
    a.remove();
    window.URL.revokeObjectURL(url);
  };

  return (
    <div>
      <h1>Reenactment Kit Builder</h1>
      <input placeholder="Century" value={century} onChange={e => setCentury(e.target.value)} />
      <input placeholder="Region" value={region} onChange={e => setRegion(e.target.value)} />
      <input placeholder="Role" value={role} onChange={e => setRole(e.target.value)} />
      <button onClick={runPipeline}>Build Kit</button>
      {result && (
        <div>
          {Object.entries(result.references).map(([item, ref]) => (
            <div key={item}>
              <p>{item} ({ref.museum})</p>
              {ref.image_url && <img src={ref.image_url} alt={item} style={{ maxWidth: '200px' }} />}
            </div>
          ))}
          <button onClick={downloadZip}>Download Images</button>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
