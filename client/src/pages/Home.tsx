import { useState } from "react";
// import { api } from "../api";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [analysis, setAnalysis] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("/analyze", {
        method: "POST", 
        body: formData, 
        headers: { "Content-Type": "multipart/form-data" } 
    });
      setAnalysis(res?.data?.result);
    } catch (err) {
      console.error(err);
      alert("Analysis failed");
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Upload Financial PDF for Analysis</h1>
      <form onSubmit={handleSubmit} className="mb-6">
        <input type="file" accept="application/pdf" onChange={e => setFile(e.target.files?.[0] ?? null)} required/>
        <button type="submit" className="ml-2 bg-blue-500 text-white px-4 py-2 rounded">Analyze</button>
      </form>
      {analysis && (
        <div className="bg-gray-100 p-4 rounded">
          <h2 className="font-bold mb-2">Analysis Result:</h2>
          <pre>{analysis}</pre>
        </div>
      )}
    </div>
  );
}
