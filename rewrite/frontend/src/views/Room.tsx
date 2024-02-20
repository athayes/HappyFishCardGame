import { useParams } from 'react-router-dom';

function Room() {
  const { roomId } = useParams<{ roomId: string }>();

  return (
    <div>
      <h2>Welcome to the room {roomId}!</h2>
    </div>
  );
}

export default Room;