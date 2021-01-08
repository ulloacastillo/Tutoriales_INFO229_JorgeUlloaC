# Tutorial (*Acercamiento*) a Redux
> ### "Requisitos del tutorial"
> Estar familiarizado con librerías UI de `Javascript`  que usen el concepto de state.

### ¿Qué es redux?
Redux es básicamente una librería de JavaScript que sirve para gestionar el `state` en aplicaciones Javascript creadas con librerías frontend, por ejemplo React, Angular, Vue o simplemente con JavaScript 'puro'.  Redux nos ayudará a poder controlar de una mejor manera el state, de tal forma que este sea centralizado, es decir, no sea necesario pasar el state enter componentes.


### ¿Cuál es la idea de Redux?
Redux, como dijimos anteriormente es utilizado para crear un state de manera global con el fin de que exista un sólo state (llamando store) y evitar crear distintos state para cada componente. La idea de Redux es poder controlar el state cuando tengas una app demasiado grande, con muchos componentes para que no tengas que preocuparte demasiado en pasar el state de componentes padres a hijos.

### ¿Cuándo usar Redux?
Redux es una herramienta muy útil dado que nos permite manejar el state de nuestra app de una manera muy elegante, sin embargo, en proyectos pequeños, sin tantos componentes, redux no es la mejor opción puesto que probablemente escribamos más código de redux que con el state propio de react, por ejemplo. Además que estaríamos haciendo un proyecto más complicado de lo que debería ser. Es por esto, que la propia página de Redux [^1] nos da unas recomendaciones de cuando usar esta librería:
> -   Cuando tengas un gran número de estados que se necesitan en muchas partes de la aplicación
>  -  La aplicación es frecuentemente actualizada.
> -   La lógica para actualizar el state puede ser un poco compleja.
> -   Es una aplicación con mucho código y varias personas están trabajando en él.

### Pros y Contras de Redux
| Pros | Contras |  
| ----------- | ----------- |  
| State Centralizado | Complejidad para aprender |  
| Fácil de *debuggear* | Verbosidad |
| Cuando la aplicación es grande, el state es fácil de manejar |  |


## Conceptos

### Store

El store es uno de los conceptos fundamentales en redux, pues es el objeto que guarda todos los state necesarios para que nuestra aplicación funcione. En otras palabras el store es un state global que tiene nuestra aplicación, en vez de tener un state por componente podemos tener un sólo state que guarde lo necesario de manera global.

> Dado que el store es global, sólo tendremos un store por aplicación. 

### Actions
Una acción es básicamente un objeto JS que te indicia que es lo que vas hacerle al state o más bien la acción (o action) describe que es lo que va a pasar en tu aplicación. Por ejemplo si tenemos un componente que lo que hace es tener un contador que podemos hacer que incremente o disminuya a través de un botón, las acciones que se pueden realizar con este componente es incrementar o reducir. 

### Reducer

Los reducers en redux son funciones que describen el cómo una acción va a modificar el state.

> Nuestros reducer serán los capaces de modificar el state dada alguna acción. Los reducer serán de la forma `(state, action) => updatedState`.


### Resumen


> 1.  El  **componente**  recibe un evento (click, por ejemplo) y emite una acción.
> 2.  Esta  **acción**, se pasa a la  _store_, que es donde se guarda el estado único.
> 3.  La  **_store_**  comunica la acción junto con el estado actual a los reducers.
> 4.  Los  **reducers**, devuelven un nuevo estado, probablemente modificado en base a la acción.
> 5.  Los componentes reciben el  **nuevo estado**  de la  store. [^2]

## Creando una mini-aplicación usando Redux y React

La aplicación que crearemos será un contador controlado por el usuario que podrá incrementar o disminuir con botones.

Como redux es sólo una librería para el control del state, necesitamos de una herramienta adicional para poder crear nuestra UI. En esta ocasión utilizaremos react y una extensión de npm para crear un proyecto de react con create-react-app.

Iniciamos el proyecto creando el directorio, para ellos nos ubicamos desde nuestro terminal en el directorio que deseemos y ejecutamos el comando
> `npx create-react-app counter-redux`

Luego, instalamos la librería redux y react-redux
> `npm install redux react-redux`

Esperamos a que se instalen y mientras tanto podemos 'limpiar' el código que nos creo create react app.
> Dentro de la carpeta `src`dejaremos sólo los archivos:
```
> src
	App.js
	index.css
	index,js
	serviceWorker.js
```

### Inicio de la Aplicación

Partiremos creando la interfaz de la aplicación en nuestro archivo `App.js` 

```diff 
> App.js
```
```d
import React from  "react";

function App() {
	return (
		<div  className="App">
			<h1>Counter 0</h1>
			<button>+</button>
			<button>-</button>
		</div>
	);
} 
export default App;
```
<img src="https://github.com/ulloacastillo/Tutoriales_INFO229_JorgeUlloaC/blob/main/Tutorial_8_REDUX/images/1.png" width="100">



A continuación en nuestro archivo `index.js`crearemos los `
Action` que serán funciones que nos retornarán un objeto describiendo que cambios se harán  los estados.
En este caso para nuestro componente Counter, necesitamos que el contador pueda aumentar y disminuir por lo que necesitaremos crear 2 'Action' uno de tipo `incrementar` y otro de tipo `disminuir`.

```diff
> index.js
```
```d
import React from  "react";
import ReactDOM from  "react-dom";
import  "./index.css";
import App from  "./App";
import reportWebVitals from  "./reportWebVitals";

// ACTIONS
const incrementar = () => {
	return {
		type: "INCREMENTAR"
	}
}
const disminuir = () => {
	return {
		type: "DISMINUIR"
	}
}
ReactDOM.render(
	<React.StrictMode>
		<App  />
	</React.StrictMode>,
	document.getElementById("root")
);
reportWebVitals();
```

Ahora con nuestras `Actions` creadas debemos crear nuestra función reducer que recibirá un `state` y una `action` y retornará un nuevo `state` dependiendo de la `action`  que reciba. 

> Debajo de la función disminuir agregaremos nuestro `reducer`   llamado `counter`.

```js
// REDUCERS
const counter = (state = 0, action) => {
	switch (action.type) {
		case  "INCREMENTAR":
			return state + 1;
		case  "DISMINUIR":
			return state - 1;
		default:
			return state;
	}
};
```

Ahora para crear nuestro store con Redux debemos importar una herramienta de la librería `redux` en nuestro archivo `index.js`.

> `import { createStore } from  "redux";`


Y para crear el store, luego de la función `counter` agregamos:
> `let store = createStore(counter);`

Si queremos ver si el state cambio, podemos agregar las siguientes lineas:

> `store.subscribe(() => console.log(store.getState()))`;
> `store.dispatch(incrementar());`

> ### Aplicamos el método `dispatch` dado que es el único método que tenemos para actualizar el state.

El resultado es
<img src="https://github.com/ulloacastillo/Tutoriales_INFO229_JorgeUlloaC/blob/main/Tutorial_8_REDUX/images/2.png" width="100">


 Ahora que tenemos ya nuestras `Actions` y nuestro `reducer` aprovecharemos de añadir un nuevo state que ocuparemos para determinar si el usuario de la aplicación se encuentra 'loggeado' o no, le llamaremos logged.
Para esto crearemos 2 carpetas nuevas dentro del directorio `src` que serán las que contendrán a los reducers de los state y los actions en archivos diferentes.

Nuestros directorios quedarán de la siguiente forma
```
> src
	> reducers
		index.js
		logged.js
		counter.js
	> actions
		index.js
	App.js
	index.css
	index,js
	serviceWorker.js
```

Dentro del archivo `counter.js` dejaremos el reducer para nuestro state contador:

```diff
> /reducers/counter.js
```
```d
const counterReducer = (state = 0, action) => {
	switch (action.type) {
		case  "INCREMENTAR":
			return state + 1;
		case  "DISMINUIR":
			return state - 1;
		default:
			return state;
	}
};
export default counterReducer;
```

```diff
> /reducers/logged.js
```
```d
const loggedReducer = (state = true, action) => {
	switch (action.type) {
		case  "SIGN_IN":
			return !state;
		default:
			return state;
	}
};
export  default loggedReducer;
```
Ahora, en el archivo `index.js` combinaremos ambos reducers en sólo objeto, con el fin de que nuestro store sea uno sólo.

```diff
> /reducers/logged.js
```
```d
import { combineReducers } from  "redux";
import loggedReducer from  "./logged";
import counterReducer from  "./counter";

const allReducers = combineReducers({
	counter: counterReducer,
	isLogged: loggedReducer,
});
export default allReducers;
```
> Utilizamos una función que nos provee redux, combineReducers, que nos permite combinar varios reducers en un sólo objeto.

Por otra parte, en el archivo `/actions/index.js` anotaremos todos nuestro actions.
```diff
> /reducers/logged.js
```
```d
export  const incrementar = () => {
	return {
		type: "INCREMENTAR",
	};
};

export  const disminuir = () => {
	return {
		type: "DISMINUIR",
	};
};

export  const log = () => {
	return {
		type: "SIGN_IN",
	};
};
```

> Nótese que hemos agregado el `Action` log que nos servirá para cambiar el estado de "LOGIN" de true a false y viceversa.

Dado que tenemos ya todos nuestros reducers, por separados y combinados, en nuestro `index.js` crearemos el store global para que nuestro(s) componentes pueda(n) utilizarlo.

```diff
> /index.js
```
```d
import React from  "react";
import ReactDOM from  "react-dom";
import  "./index.css";
import App from  "./App";
import reportWebVitals from  "./reportWebVitals";
import { createStore } from  "redux";
import allReducer from  "./reducers/index";
import { Provider } from  "react-redux";

const store = createStore(allReducer);

ReactDOM.render(
	<React.StrictMode>
		<Provider  store={store}>
			<App  />
		</Provider>
	</React.StrictMode>,
document.getElementById("root")
);
reportWebVitals();
```
> Notemos que estamos importando un nuevo componente desde `react-redux`. Este componente llamado Provider es utilizado para que todos los hijo de él puedan tener acceso al store sin pasar por `props`.
> `<Provider  store={store}>`


Ahora que tenemos ya listo el arranque de nuestra aplicación, podemos crear el componente principal de nuestra aplicación: `App.js`

```diff
> /App.js
```
```d
import React from  "react";
import { useSelector, useDispatch } from  "react-redux";
import { incrementar, disminuir, log } from  "./actions/index";

function App() {
	const counter = useSelector((state) => state.counter);
	const isLogged = useSelector((state) => state.isLogged);
	const dispatch = useDispatch();
	return (
		<div  className="App">
			{isLogged ? (
				<div>
					<h3>Bienvenido Usuario</h3>
					<button  onClick={() => dispatch(log())}>LOG OUT</button>
				</div>
			) : (
				<div>
					<h3>Por favor inicie sesion</h3>
					<button  onClick={() => dispatch(log())}>LOG IN</button>
				</div>
			)}
			<h1>Counter {counter}</h1>
			<button  onClick={() => dispatch(incrementar())}>+</button>
			<button  onClick={() => dispatch(disminuir())}>-</button>
		</div>
	);
}
export  default App;
```
> Las funciones useSelector y useDispatch importadas desde `react-redux`
 sirven para obtener una porción del state guardado en el store y para poder ejecutar nuestras `Actions` como si fueran unos eventsHandlers.

 
EL RESULTADO ES:
<img src="https://github.com/ulloacastillo/Tutoriales_INFO229_JorgeUlloaC/blob/main/Tutorial_8_REDUX/images/3.png" width="100">
<img src="https://github.com/ulloacastillo/Tutoriales_INFO229_JorgeUlloaC/blob/main/Tutorial_8_REDUX/images/4.png" width="100">
<img src="https://github.com/ulloacastillo/Tutoriales_INFO229_JorgeUlloaC/blob/main/Tutorial_8_REDUX/images/5.png" width="100">
### Referencias

[^1]: https://redux.js.org/tutorials/essentials/part-1-overview-concepts#when-should-i-use-redux
[^2]: http://blog.enriqueoriol.com/2018/08/que-es-redux.html
