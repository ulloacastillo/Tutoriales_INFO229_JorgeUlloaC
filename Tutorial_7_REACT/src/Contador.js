import React, { useState } from "react";

function Contador(props) {
  const [cont, setCont] = useState(0);

  const handleClick = () => {
    setCont(cont + 1);
  };

  return (
    <div>
      <h1>Contador: {props.nombre}</h1>
      <p>El contador esta en {cont}</p>
      <button onClick={handleClick}>Aumentar Contador</button>
    </div>
  );
}

export default Contador;
