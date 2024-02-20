import React, { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCat } from '@fortawesome/free-solid-svg-icons';
import IconSelector from '../components/IconSelector';

function JoinRoom() {
  const { roomId } = useParams();
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [icon, setIcon] = useState(faCat);

  const joinRoom = () => {
    if (name !== '') {
      navigate(`/room/${roomId}`, { state: { name, icon } });
    }
  };
  
  const handleNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setName(event.target.value);
  };


  return (
    <div className="JoinRoom">
      <h2>Join Room {roomId}</h2>
      <input
        type="text"
        value={name}
        onChange={handleNameChange}
        placeholder="Enter your name"
      />
      <p>Choose an icon:</p>
      <IconSelector onIconChange={setIcon} />
     
      <button onClick={joinRoom}>
        Join Room
      </button>
    </div>
  );
}

export default JoinRoom;