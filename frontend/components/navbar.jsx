import React from "react"; 
import ReactDOM from "react-dom"; 
import Navbar from "./navbar/index";

window.onload = function() {
    ReactDOM.render(<Navbar/>, document.getElementById("navbar"));
};