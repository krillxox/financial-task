import { useState } from "react";
// import { api } from "../api";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [query, setQuery] = useState<string>("");
  const [analysis, setAnalysis] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);
    formData.append("query", query)
    try {
      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/analyze`, {
        method: "POST", 
        body: formData, 
        // headers: { "Content-Type": "multipart/form-data" },
        credentials: "include"
    });
      if(response.ok){
        const data = await response.json()
        console.log(data);
        
        setAnalysis(data?.result.analysis);
      }
    } catch (err) {
      console.error(err);
      alert("Analysis failed");
    }
  };

  return (
    <div className="h-full w-full flex flex-col items-center justify-center p-8">
      <h1 className="text-3xl font-bold mb-6">Upload Financial PDF for Analysis</h1>
      <form onSubmit={handleSubmit} className="h-1/2 w-1/2 mb-6 flex flex-col items-center justify-around">
        <input className="p-4 gap-2 border-2 rounded-md w-full" type="file" accept="application/pdf" onChange={e => setFile(e.target.files?.[0] ?? null)} required/>
        <input className="p-4 gap-2 border-2 rounded-md w-full" type="text" onChange={e => setQuery(e.target.value)} placeholder="Enter query"/>
        <button type="submit" className="ml-2 bg-blue-500 text-white px-4 py-2 rounded">Analyze</button>
      </form>
      {analysis && (
        <div className="bg-gray-100 p-4 rounded w-3/4">
          <h2 className="font-bold mb-2">Analysis Result:</h2>
          <pre className="h-full w-full overflow-auto">{analysis}</pre>
        </div>
      )}
    </div>
  );
}
