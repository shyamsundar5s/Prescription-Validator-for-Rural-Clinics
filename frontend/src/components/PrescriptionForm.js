import React, { useState } from 'react';

function PrescriptionForm() {
  const [prescriptionText, setPrescriptionText] = useState("");
  const [symptoms, setSymptoms] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const response = await fetch('/validate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prescription_text: prescriptionText, symptoms: symptoms.split(", ") }),
    });
    const data = await response.json();
    setResult(data);
  };

  return (
    <div>
      <textarea
        placeholder="Enter or Paste Prescription Text"
        value={prescriptionText}
        onChange={(e) => setPrescriptionText(e.target.value)}
      />
      <input
        type="text"
        placeholder="Enter symptoms, comma-separated"
        value={symptoms}
        onChange={(e) => setSymptoms(e.target.value)}
      />
      <button onClick={handleSubmit}>Validate</button>
      {result && (
        <div>
          <h3>Validation Results</h3>
          <p>Medicines: {result.medicines.join(", ")}</p>
          <p>Warnings: {result.warnings.join(" | ")}</p>
        </div>
      )}
    </div>
  );
}

export default PrescriptionForm;
