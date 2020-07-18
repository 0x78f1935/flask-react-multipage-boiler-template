import React from "react"; 
import ReactDOM from "react-dom";
import AboutPage from './about/index';

window.addEventListener("load",
    ReactDOM.render(<AboutPage />, document.getElementById("content"))
);