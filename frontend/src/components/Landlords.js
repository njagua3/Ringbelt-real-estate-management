import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Landlords = () => {
  const [landlords, setLandlords] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLandlords = async () => {
      setLoading(true);
      try {
        const response = await axios.get('/api/landlords');
        setLandlords(response.data);
      } catch (error) {
        console.error('Error fetching landlords:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchLandlords();
  }, []);

  return (
    <div>
      <h2>Landlords</h2>
      {loading ? <p>Loading...</p> : (
        <ul>
          {landlords.map(landlord => (
            <li key={landlord.id}>{landlord.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Landlords;
