import React from "react"; 
import ReactDOM from "react-dom";
import { Container, Typography } from '@material-ui/core';

class App extends React.Component {
    render () {
        return (
            <Container>
                <Typography>
                    Hello React Multi page application!
                </Typography>
            </Container>
        );
    } 
}

ReactDOM.render(<App />, document.getElementById("content"));