import  { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { sillyGameName } from '../util/sillyWords';

function Home() {
  const navigate = useNavigate();
  const [sillyName, setSillyName] = useState('Happy Fish Card Game');

  useEffect(() => {
    setSillyName(sillyGameName());
  }, []);

  return (
    <div className="Home">
      <h2>{sillyName}</h2>
      <button
        className="btn pink-button"
        onClick={() => navigate('/create')}
        style={{ marginTop: '20px' }}
      >
        Create a New Game
      </button>
      <button
        className="btn pink-button"
        onClick={() => navigate('/join')}
        style={{ marginTop: '20px' }}
      >
        Join a Game
      </button>
    </div>
  );
}

export default Home;