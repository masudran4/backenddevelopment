
import { useEffect } from 'react';
const API_URL = "http://192.168.0.195:8000/";


export function AddPerson(prop){
    return (
        <div>
            <h1 className="text-green-500" onCl>{prop.name}</h1>
            {prop.children}
        </div>
        
    );
}


export function ApiCall() {
    useEffect(() => {
      fetch(API_URL)
        .then(response => response.json())
        .then(data => console.log("Todos from API:", data))
        .catch(error => console.error("Error:", error));
    }, []);
  
    return <h1>Check browser console for todo list</h1>;
  }

