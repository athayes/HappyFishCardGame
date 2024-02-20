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
      <p>If you don't have a room ID, please navigate directly to the URL provided by the host.</p>
    </div>
  );
}

export default Join;