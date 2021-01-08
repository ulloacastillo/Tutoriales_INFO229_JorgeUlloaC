import React from "react";
import ReactDOM from "react-dom";
import Contador from "./Contador.js";

ReactDOM.render(
  <React.StrictMode>
    <div>
      <Contador nombre="Contador Número 1" />
      <Contador nombre="Contador 2" />
    </div>
  </React.StrictMode>,
  document.getElementById("root")
);
