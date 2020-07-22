import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Card} from 'react-bootstrap';
import Clock from '../../widgets/clock';


export default class HomePage extends React.Component {
    render () {
        return (
            <Container style={{ marginTop: '15px'}}>
                <Card className="text-center">
                    <Card.Footer className="text-muted"><Clock/></Card.Footer>
                    <Card.Body>
                        <Card.Title>Multi Page Flask React Boiler Template</Card.Title>
                        <Card.Text>
                            The boiler template is correctly installed. From here its all on you.<br/>
                            Change however, whatever, whenever, wherever you want to you own likings.
                        </Card.Text>
                    </Card.Body>
                </Card>
            </Container>
        );
    } 
}