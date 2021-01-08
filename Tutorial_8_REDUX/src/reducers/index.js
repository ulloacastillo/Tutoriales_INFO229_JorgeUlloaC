import { combineReducers } from "redux";
import loggedReducer from "./logged";
import counterReducer from "./counter";

const allReducers = combineReducers({
  counter: counterReducer,
  isLogged: loggedReducer,
});
export default allReducers;
