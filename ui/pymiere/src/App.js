import logo from './logo.svg';
import './App.css';
import ImageUIPage from './ImageUIPage'
import ProjectSelectPage from './ProjectSelectPage'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import CenterImagePage from './CenterImagePage';

function App() {
  /*return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  ); */

  return (
    <Router>
      <Switch>
      <Route path="/image">
        <ImageUIPage />
      </Route>
      <Route path="/">
        <ProjectSelectPage />
      </Route>
    </Switch>
    </Router>

  )
}

export default App;
