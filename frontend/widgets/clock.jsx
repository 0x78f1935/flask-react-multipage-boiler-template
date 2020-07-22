import React, { Component } from "react"; 

export default class Clock extends Component {
    constructor(props) {
        super(props);
        this.state = {date: new Date()};
    }
  
    componentDidMount() {
        this.timerID = setInterval(
            () => this.tick(),
            1000
        );
    }
  
    componentWillUnmount() {
        clearInterval(this.timerID);
    }
  
    tick() {
        this.setState({
            date: new Date()
        });
    }
  
    render() {
        console.log(this.state.date.toLocaleTimeString())
        return (
            <div>
                <h1>Hello, world!</h1>
                <h2>It is {this.state.date ? this.state.date.toLocaleTimeString() : null}.</h2>
            </div>
        );
    }
}