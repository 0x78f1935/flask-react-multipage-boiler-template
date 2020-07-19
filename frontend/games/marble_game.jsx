import React from "react"; 
import ReactDOM from "react-dom"; 
import Unity, { UnityContent } from "react-unity-webgl";

const unityContent = new UnityContent(
    "static/webGL/Marbles/Build.json",
    "static/webGL/Marbles/UnityLoader.js"
);

window.addEventListener("load",
    ReactDOM.render(<Unity unityContent={unityContent} />, document.getElementById("unity"))
);