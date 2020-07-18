import React from "react"; 
import ReactDOM from "react-dom"; 
import NavbarComponent from "./navbar/index";

window.addEventListener("load",
    ReactDOM.render(<NavbarComponent/>, document.getElementById("navbar"))
);