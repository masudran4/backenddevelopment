import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { AddPerson } from './componants/utils'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card bg-base-100 w-96 shadow-xl">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="text-gray-600">
        Click on the Vite and React logos to learn more
      </p>
      <button className="btn btn-secondary outline">Secondary</button>
      <AddPerson name="Masud">
        <p className='text-amber-400'>He is having 5 years of experience as qa engineer!</p>
      </AddPerson>
    </>
  )
}

export default App
