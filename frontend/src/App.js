import React from 'react';
import PrescriptionForm from './components/PrescriptionForm';
import OCRUploader from './components/OCRUploader';

function App() {
  return (
    <div>
      <h1>Prescription Validator</h1>
      <OCRUploader />
      <PrescriptionForm />
    </div>
  );
}

export default App;
