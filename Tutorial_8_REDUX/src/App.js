import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { incrementar, disminuir, log } from "./actions/index";

function App() {
  const counter = useSelector((state) => state.counter);
  const isLogged = useSelector((state) => state.isLogged);
  const dispatch = useDispatch();

  return (
    <div className="App">
      {isLogged ? (
        <div>
          <h3>Bienvenido Usuario</h3>
          <button onClick={() => dispatch(log())}>LOG OUT</button>
        </div>
      ) : (
        <div>
          <h3>Por favor inicie sesion</h3>
          <button onClick={() => dispatch(log())}>LOG IN</button>
        </div>
      )}
      <h1>Counter {counter}</h1>
      <button onClick={() => dispatch(incrementar())}>+</button>
      <button onClick={() => dispatch(disminuir())}>-</button>
    </div>
  );
}
export default App;
