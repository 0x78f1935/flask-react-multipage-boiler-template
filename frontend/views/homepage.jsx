import React from "react"; 
import ReactDOM from "react-dom";
import HomePage from './homepage/index';

window.addEventListener("load",
    ReactDOM.render(<HomePage />, document.getElementById("content"))
);