import Addnew from './Add.jsx'
// import './Add.jsx'
import './App.css'

function App() {
  return (
    <>
    <header>
      Todo
      <button onClick={Addnew()}>Add new work</button>
    </header>
    
    <div className='todo table'>
      <table>
        <thead>
          <tr>
            <th>Work or what to do</th>
            <th>done  or not</th>

          </tr>
        </thead>

        <tr>
          <td>work 1</td>
          <td>done</td>
        </tr>
        <tr>
          <td>work 2</td>
          <td>done</td>
        </tr>
        <tr>
          <td>work 3</td>
          <td>not done</td>
        </tr>
      </table>
    </div>
    </>
  )
}

export default App
