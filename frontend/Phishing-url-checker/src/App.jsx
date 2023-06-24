import React from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
} from "react-router-dom";
import EnterUrl from './pages/EnterUrl';


function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<EnterUrl />} />
        </Routes>
      </Router>
    </div>
  )
}

export default App