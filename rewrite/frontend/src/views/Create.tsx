// Home.js
import { useState, useEffect } from 'react';
// import axios from 'axios';
import { sillyGameName } from '../util/sillyWords';

function Home() { 
  const [name, setName] = useState('');

  async function createRoom() {
    
    // if (name === '') {
    //   alert('Enter your name');
    //   return;
    // }
    
    // const response = await axios.post(
    //   `${process.env.REACT_APP_BACKEND_URL}/CreateLobby`,
    //   { name }
    // );
    // if (
    //   response.data === 'Name taken; pick a new name!' ||
    //   response.data === 'Too many players'
    // ) {
    //   alert(response.data);
    // } else {
    //   const { lobbyId } = response.data;
    //   setCookie({ name, lobbyId });
    //   await joinRoom({ name, id: lobbyId });
    //   // Navigate to the Lobby route
    //   // This will depend on your routing setup
    // }
  }

  return (
    <div className="Home">
      <h2>Create game</h2>
      <label htmlFor="name">Your name</label>
      <input
        onKeyUp={(e) => e.key === 'Enter' && createRoom()}
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="joinLobbyEnterName"
        type="text"
        id="name"
      />
      <button
        className="btn pink-button"
        onClick={createRoom}
        style={{ marginTop: '20px' }}
      >
        Create Private Room
      </button>
    </div>
  );
}

export default Home;