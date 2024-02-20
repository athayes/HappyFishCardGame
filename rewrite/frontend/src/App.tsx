import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './views/Home';
import Room from './views/Room';
import Game from './views/Game';
import Create from './views/Create';
import Join from './views/Join';
import JoinRoom from './views/JoinRoom';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} /> // Add the 'Home' component
        <Route path="/room" element={<Room />} />
        <Route path="/game" element={<Game />} />
        <Route path="/create" element={<Create />} />
        <Route path="/join" element={<Join />} />
        <Route path="/join/:roomId" Component={JoinRoom} />
      </Routes>
    </Router>
  );
}

export default App;