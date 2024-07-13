import React, { useState } from 'react';
import axios from 'axios';

function JobSearchForm() {
  const [criteria, setCriteria] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('http://localhost:5000/search_jobs', { criteria });
    setResult(response.data);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Job Search Criteria:
          <input type="text" value={criteria} onChange={(e) => setCriteria(e.target.value)} />
        </label>
        <button type="submit">Search</button>
      </form>
      {result && <div><pre>{JSON.stringify(result, null, 2)}</pre></div>}
    </div>
  );
}

export default JobSearchForm;