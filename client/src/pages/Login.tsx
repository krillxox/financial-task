import { useState } from "react";
// import { api } from "../api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // await fetch(`${import.meta.env.VITE_BACKEND_URL}/auth/login`, {
    //   method: "POST"
    // })
    try {
      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/auth/login`, { 
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password }),
        credentials: "include"  
    });
      navigate("/");
    } catch (err) {
      console.error(err);
      alert("Login failed");
    }
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <form className="bg-white p-6 rounded shadow-md w-80" onSubmit={handleSubmit}>
        <h2 className="text-2xl font-bold mb-4">Login</h2>
        <input type="email" placeholder="Email" className="border p-2 mb-2 w-full" value={email} onChange={e=>setEmail(e.target.value)} required/>
        <input type="password" placeholder="Password" className="border p-2 mb-4 w-full" value={password} onChange={e=>setPassword(e.target.value)} required/>
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded w-full">Login</button>
      </form>
    </div>
  );
}
