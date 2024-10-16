import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Properties = () => {
  const [properties, setProperties] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProperties = async () => {
      setLoading(true);
      try {
        const response = await axios.get('/api/properties');
        setProperties(response.data);
      } catch (error) {
        console.error('Error fetching properties:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchProperties();
  }, []);

  return (
    <div>
      <h2>Properties</h2>
      {loading ? <p>Loading...</p> : (
        <ul>
          {properties.map(property => (
            <li key={property.id}>{property.address}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Properties;
