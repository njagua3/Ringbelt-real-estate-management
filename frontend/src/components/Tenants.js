import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Tenants = () => {
  const [tenants, setTenants] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTenants = async () => {
      setLoading(true);
      try {
        const response = await axios.get('/api/tenants');
        setTenants(response.data);
      } catch (error) {
        console.error('Error fetching tenants:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchTenants();
  }, []);

  return (
    <div>
      <h2>Tenants</h2>
      {loading ? <p>Loading...</p> : (
        <ul>
          {tenants.map(tenant => (
            <li key={tenant.id}>{tenant.name} - ${tenant.due_amount.toFixed(2)}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Tenants;
