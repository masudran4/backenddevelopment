import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './index.css'
import { AddPerson, ApiCall } from './componants/utils'
import {Menu} from './componants/Menu'
import { Services } from './componants/Services'
import { Card } from './componants/Card'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Menu />
    <div className='m-5'>
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

              <div className='card card-lg caret-indigo-50'>
              <ApiCall />
              </div>
              <div className='flex flex-col'>
                    <div role="tablist" className="tabs tabs-lift">
                    <Services />
                    </div>
                    <Card />
              </div>
              
    </div>
    </>
  )
}

export default App
