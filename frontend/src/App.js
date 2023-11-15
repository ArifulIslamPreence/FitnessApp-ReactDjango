//import logo from './logo/logo.svg';
import fitness_main_logo from './logo/fitness_main_logo.png'
import './App.css';

function App() {
  return (
  <div className="App">
       <header className="App-header">
        <img src={fitness_main_logo} className="App-logo" alt="logo" />
         <h1>Fitness App</h1>
       </header>
       <div className="Features">
         <div className="ContactUs">
           <h2>Exercise Set</h2>
           <p>Timer</p>
           <p>Record</p>
         </div>
       </div>
     </div>

  );
}

export default App;
