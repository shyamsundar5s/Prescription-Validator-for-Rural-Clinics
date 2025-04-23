import React, { useState } from 'react';

function OCRUploader() {
  const [text, setText] = useState("");

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/ocr', {
      method: 'POST',
      body: formData,
    });
    const data = await response.json();
    setText(data.text);
  };

  return (
    <div>
      <input type="file" onChange={handleUpload} />
      <p>Extracted Text: {text}</p>
    </div>
  );
}

export default OCRUploader;
