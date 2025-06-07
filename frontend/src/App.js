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

  return (
    <div>
      <h1>Reenactment Kit Builder</h1>
      <input placeholder="Century" value={century} onChange={e => setCentury(e.target.value)} />
      <input placeholder="Region" value={region} onChange={e => setRegion(e.target.value)} />
      <input placeholder="Role" value={role} onChange={e => setRole(e.target.value)} />
      <button onClick={runPipeline}>Build Kit</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}

export default App;
