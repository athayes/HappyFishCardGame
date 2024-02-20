import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Join() {
  const [roomId, setRoomId] = useState('');
  const navigate = useNavigate();

  const handleRoomIdChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setRoomId(event.target.value);
  };

  const handleJoinRoom = () => {
    navigate(`/join/${roomId}`);
  };

  return (
    <div className="Join">
      <h2>Join a Game</h2>
      <input
        type="text"
        value={roomId}
        onChange={handleRoomIdChange}
        placeholder="Enter room ID"
      />
      <button onClick={handleJoinRoom}>Join Room</button>
      <p>Don't have a room ID? That's okay! The host might have sent you a link - follow it to join the game!</p>  
      </div>
  );
}

export default Join;