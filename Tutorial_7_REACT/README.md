# *Tutorial (Acercamiento) a React*

> "Requisitos del tutorial" : Conocimientos básicos de JavaScript y HTML

### ¿Qué es React?
> React es una de las librerías más conocidas de JavaScript utilizada para crear interfaces gráficas. React te permite crear porciones de código llamados componentes que servirán para aislar secciones de tu interfaz gráfica y poder reutilizarlo las veces que quieras.
### Hola Mundo en React
> La versión más básica de un Hola mundo en React está dada por el siguiente código `HTML`
```d
<!DOCTYPE  html>
<html  lang="en">
	<head>
		<meta  charset="utf-8"  />
		<title>Hola Mundo</title>
		<script  src="https://unpkg.com/react@16/umd/react.development.js"></script>
		<script  src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
		<script  src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
	</head>
	<body>
		<div  id="root"></div>
		<script  type="text/babel">
		ReactDOM.render(<h1>Hello World</h1>,document.getElementById("root"));
		</script>
	</body>
</html>
```
> Las lineas:
````d
<script  src="https://unpkg.com/react@16/umd/react.development.js"></script>
<script  src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
<script  src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
````
>  Importan todo lo necesario para poder ejecutar código JavaScript en un Navegador.  Los 2 primeros script son para importar <a href="https://medium.com/programming-sage/react-vs-react-dom-a0ed3aea9745" > react y react DOM</a> que nos servirá para poder escribir código react y renderizarlo en el navegador respectivamente. El tercer script importa una herramienta llamada  <a href="https://babeljs.io/"> Babel</a> de la cual hablaremos más adelante.

> Finalmente tenemos el`<div>` con el id `#root`que es el punto de entrada para nuestra aplicación, aquí es donde nuestra app cobra vida.
> En el  tag `<script type="text/babel">`  escribiremos todo nuestro código react para dar funcionalidad a nuestra aplicación.


### ¿Qué es JSX?
> Si vemos la línea de código `ReactDOM.render(<h1>Hello World</h1>,document.getElementById("root"));` que escribimos en la sección Hola mundo en react, podemos observar que esto esta dentro de una etiqueta `script`, lo cuál nos indica que es código de tipo `JavaScript`, sin embargo, dentro del método render() hay etiquetas `HTML`. Esto es un poco raro, dado que `JavaScript`no nos permite escribir `HTML` como tal dentro del código. Sin embargo, esto funciona debido a que el `<h1>Hello World</h1>` no es ni un String ni código `HTML`, como la mayoría puede estar pensando, sino que es algo que se llama `JSX`.  `JSX`Es una manera de escribir código JavaScript pero de una forma más sencilla y lo mas parecido a `HTML`, la idea de esto nace de que no necesitemos escribir código `JavaScript` puro para poder crear componentes como si lo estuviéramos haciendo de la manera convencional.
> Lo bueno de `JSX` es que nos permite "mezclar" código `JavaScript` con "etiquetas" `HTML`. Por ejemplo si queremos mostrar la suma de manera dinámica podemos hacerlo en `JSX` de la siguiente forma:
 ```d
let x = 5;
let y = 7;
ReactDOM.render(<h1>Hello World {x+y} </h1>,document.getElementById("root"));
 ```
 > Este código que no es `JavaScript` será traducido con el compilador `Babel` para que el navegador pueda entenderlo. Por ejemplo si hacemos el siguiente código en react:
```d
var nav = (
    <ul id="nav">
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
    </ul>
);
```
> Babel lo traducirá al siguiente código `JavaScript``
```d
var nav = React.createElement("ul", {id: "nav"}, 
	React.createElement("li", null, React.createElement("a", {href: "#"}, "Home")),
	React.createElement("li", null,React.createElement("a", {href: "#"}, "About")
));
```

Como vemos, Babel y JSX nos pueden ayudar mucho a que nuestro código sea mucho más limpio, legible y fácil de escribir.

### Create React App
> Luego de esta breve introducción a react, les propongo iniciar un proyecto muy pequeño que consistirá en hacer un pequeño contador que terminará viéndose así:
> INSERTAR GIF DEL PROYECTO TERMINADO
> - Para esto usaremos una herramienta que nos provee react llamada create react app. "**<a href="https://es.reactjs.org/docs/create-a-new-react-app.html">Create React App</a>**  configura tu ambiente de desarrollo de forma que puedas usar las últimas características de Javascript, brindando una buena experiencia de desarrollo, y optimizando tu aplicación para producción".
> - Para utilizarla necesitaremos instalar <a href="https://nodejs.org/en/">NodeJS</a> en su versión estable.

> Una vez instalado NodeJs, iremos hasta nuestro terminal, en el directorio que deseemos, y anotaremos los siguiente comandos.

```diff
-> npx create-react-app contador
-> cd contador
-> npm start
```
> Esto nos abrirá una nueva ventana en el navegador con la aplicación desplegada. Luego con nuestro editor de código preferido abriremos la carpeta `contador` y nos dirigiremos hacia la carpeta `src`, es ahí donde se encuentra el código que desarrollaremos en este 'tutorial'.
> Ahora abriremos el archivo `index.js` y cambiaremos su contenido por:
```diff 
> index.js
```
```d
import React from  "react";
import ReactDOM from  "react-dom";

ReactDOM.render(
	<React.StrictMode>
		<div>
			<h1>Contador</h1>
			<p>El contador esta en 0</p>
			<button>Aumentar Contador</button>
		</div>
	</React.StrictMode>,
	document.getElementById("root")
);
```
Lo que da como resultado
![alt text](https://github.com/ulloacastillo/Tutorial_7_react/blob/master/images/2.png)
> Este será el archivo donde estará lo más importante del proyecto.
### Componentes y *props*
> Un componente en react  es una pieza de código que es reusable e independiente, un componente cumple el mismo propósito que una función de `JavaScript`, pero un componente debe retornar "HTML" (pero ya sabemos que es JSX) para que sea renderizado por el método `render()`.
> En nuestra aplicación crearemos un componente que estará encargado de crear un contador y un botón para aumentar este.
> Para ello crearemos, en la carpeta `src` un nuevo archivo llamando `Contador.js` (los nombres de los componentes, por convención, suelen empezar con mayúsculas).
> Dentro de este archivo anotaremos lo siguiente:

```diff 
> Contador.js
```
```d
import React from  "react";
function Contador() {
	return (
		<div>
			<h1>Contador</h1>
			<p>El contador esta en 0</p>
			<button>Aumentar Contador</button>
		</div>
	);
}
export  default Contador;
```

> Ahora para poder utilizar este componente, tenemos que importarlo en `
index.s` y remplazar el código que creaba el contador.

```diff 
> index.js
```
```d
import React from  "react";
import ReactDOM from  "react-dom";
import Contador from  "./Contador.js";

ReactDOM.render(
	<React.StrictMode>
		<div>
			<Contador  />
		</div>
	</React.StrictMode>,
	document.getElementById("root")
);
```
> Esto dará el mismo resultado que la imagen anterior.

Pero si por ejemplo, queremos agregar más contadores simplemente debemos hacer otro llamado al componente.
```diff 
> index.js
```
```d
import React from  "react";
import ReactDOM from  "react-dom";
import Contador from  "./Contador.js";

ReactDOM.render(
	<React.StrictMode>
		<div>
			<Contador  />
			<Contador  />
		</div>
	</React.StrictMode>,
	document.getElementById("root")
);
```
![alt text](https://github.com/ulloacastillo/Tutorial_7_react/blob/master/images/3.png)
### Props
> Ahora que ya hemos creado nuestro primer componente en react, podemos utilizar un concepto importante de los componentes en react: los *props* o propiedades de un componente son algo así como los parámetros de una función que nos van ayudar a que con un sólo componente podamos crear multiples elementos con distinta identidad en nuestra interfaz.

En nuestro proyecto podemos utilizar los props en nuestro componente Contador para que cada Contador pueda tener un nombre distinto.
Para ello en nuestro archivo `index.js` tenemos que pasarle un prop a nuestro componente.
```diff 
> index.js
```
```d
import React from  "react";
import ReactDOM from  "react-dom";
import Contador from  "./Contador.js";

ReactDOM.render(
	<React.StrictMode>
		<div>
			<Contador nombre="Contador Número 1" />
			<Contador nombre="Contador 2"/>
		</div>
	</React.StrictMode>,
	document.getElementById("root")
);
```
Ahora también debemos modificar nuestro componente para que pueda renderizar en nombre que le pasamos por props.

```diff 
> Contador.js
```
```d
import React from  "react";
function Contador(props) {
	return (
		<div>
			<h1>Contador: { props.nombre }</h1>
			<p>El contador esta en 0</p>
			<button>Aumentar Contador</button>
		</div>
	);
}
export default Contador;
```
![alt text](https://github.com/ulloacastillo/Tutorial_7_react/blob/master/images/4.png)
### State
El state en react es otra de las propiedades fundamentales que hacen que esta librería sea tan popular, el `state` es un objeto `JavaScript` que contiene información esencial de un componente y que nos permite que estos puedan ser dinámicos, cambiando cuando el usuario activa un evento. 

> A continuación usaremos state para poder mostrar el contador en pantalla.

```diff 
> Contador.js
```
```d
import React, { useState } from  "react";

function Contador(props) {

	const [cont, setCont] = useState(5);
	
	return (
		<div>
			<h1>Contador: {props.nombre}</h1>
			<p>El contador esta en {cont}</p>
			<button>Aumentar Contador</button>
		</div>
	);
}
export  default Contador;
```
![alt text](https://github.com/ulloacastillo/Tutorial_7_react/blob/master/images/5.png)

> Como vemos el contador esta iniciado en 5


En las versiones antiguas de react, para usar state debíamos crear un componente de clase, que no veremos en este tutorial, dado que desde react 16.8 no es necesario usar componentes de clases. Para eso react creo una herramienta llamada useState que nos permite crear state en componentes funcionales (como los hemos trabajado hasta el momento.

Para crear estados con `useState` debemos hacerlo de la siguiente forma:
```d
const [ nombreEstado, setNombreEstado ] = useState(estadoInicial);
```

`nombreEstado` será la variable que contendrá el estado de la función y `setNombreEstado` es una función que modifica el estado.

> **Nota Bene**: Un componente puede tener más de un state o no tener state. No es obligación que tenga un sólo estado.

Como en nuestro caso nosotros estamos construyendo un contador, para inicializar nuestro estado lo más lógico es que este contador inicie en 0. Por lo que nuestro estado debería verse de la siguiente forma.
```d
const [ cont, setCont ] = useState(0);
```

Esto hará que nuestro contador parta en 0 cada vez que refresquemos la página.

> **Observación** : Diferencia entre props y state.
> Como hemos estado viendo, las props y el state, en react, son cosas son completamente distintas, sin embargo, puede generar confusión al momento de crear un proyecto. 
> Usaremos el state para guardar datos que necesitas para controlar tu página, por ejemplo, listas de clientes, tareas, algún contador, etc.
> Usaremos props para pasar datos entre componentes o para darle identidad a nuestros componentes (poner títulos distintos en componentes diferentes).

### Eventos 

Con manejar un evento en una aplicación nos referimos a capturar algún cambio en nuestra aplicación que fue producido por el usuario, por ejemplo, presionar un botón, enviar un formulario, escribir en una caja de texto, etc.
> La forma convencional de manejar eventos con `HTML`y `JavaScript`es de la siguiente forma:
```html
<button onclick="handleClick()">
	Click Aqui
</button>
```
> Por otro lado en react (o más bien JSX)

```html
<button onClick={handleClick}>
  Activate Lasers
</button>
```
> Las diferencias son que en JSX usamos camelCase para nombrar los eventos (onClick, onSubmit, onChange, etc) y al pasar el manejador de eventos lo hacemos como función (entre corchetes { } ).

En nuestro proyecto usaremos manejadores de eventos para poder cambiar el estado de nuestro componente y así poder aumentar en 1 el número del contador, para esto en nuestro botón tenemos que agregar el evento que deseamos capturar, en este caso el evento es un click.
```html
<button  onClick={handleClick}>Aumentar Contador</button>
```
> `handleClick` será la función que aumentara el contador (state) en 1.

Para esto crearemos la función `handleClick`

```d
const handleClick = () => {
	setCont(cont + 1);
};
```

> Esta función, cada vez que se realiza un click sobre el botón actualizará en state, aumentando el contador `cont`.

Finalmente nuestro archivo `Contador.js` nos quedará:
```diff 
> Contador.js
```
```d
import React, { useState } from  "react";

function Contador(props) {
	const [cont, setCont] = useState(0);

	const handleClick = () => {
		setCont(cont + 1);
	};

	return (
		<div>
			<h1>Contador: {props.nombre}</h1>
			<p>El contador esta en {cont}</p>
			<button  onClick={handleClick}>Aumentar Contador</button>
		</div>
	);
}

  

export  default Contador;
```

Con esto estamos terminamos este pequeño acercamiento a react, cualquier duda pueden consultar el código que esta dentro de este repositorio :)

### Map,  Filter and Reduce

Esto es una sección aparte para mostrarte 2 métodos para listas que pueden ser muy útiles al momento de crear aplicaciones.

**Map**: `list.map(function)` básicamente dada una lista, le aplica la función a cada elemento retornando un elemento nuevo.
Por ejemplo:
```
let lista = [1, 2, 3, 4, 5];
lista.map(function(elem){
	return elem ** 2;
})
```
> Esto nos retornará una nueva lista con los cuadrados de los elementos de lista: `[1, 4, 9, 16, 25]`.

**Filter**: `list.filter(function)` tal como lo dice su nombre, filter recibe una función (que devuelve un booleano)  y retorna los elementos de la lista que si cumplan la condición.
Por ejemplo:
> Para la misma lista `let lista = [1, 2, 3, 4, 5]`si aplicamos `lista.filter(function(e){return e > 2})` nos devolverá la lista `[3, 4, 5]`.

**Reduce**: `list.reduce(function, initialValue)` Lo que hace es reducir toda la lista a un único valor (de cualquier tipo).
Por ejemplo:
```
let lista = [1, 2, 3, 4, 5];
lista.reduce(function(x, acum){
	return (x + acum);}, 0)
```

> Dada la lista y el valor inicial 0, `reduce` suma todos lo elementos de la lista, por lo que este método devolvería 15.

<img src="https://www.globalnerdy.com/wordpress/wp-content/uploads/2016/06/map-filter-reduce-in-emoji-1.png"  width="400"/>
<a href="https://www.globalnerdy.com/wordpress/wp-content/uploads/2016/06/map-filter-reduce-in-emoji-1.png">Fuente</a>
