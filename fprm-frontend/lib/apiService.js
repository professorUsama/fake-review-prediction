export const apiClient = async (endpoint) =>{
  const res = await fetch(`http://localhost:8000/api${endpoint}`);
  if(!res.ok) {
    throw new Error(`Faild to fetch ${endpoint}`);
  };
  return res.json();
};