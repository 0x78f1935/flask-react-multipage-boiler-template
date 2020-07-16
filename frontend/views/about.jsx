import React from "react"; 
import ReactDOM from "react-dom";
import { Container, Typography } from '@material-ui/core';

alert("Hello About!");

class App extends React.Component {
    render () {
        return (
            <Container>
                <Typography>
                    Hello About!
                </Typography>
            </Container>
        );
    } 
}

ReactDOM.render(<App />, document.getElementById("content"));