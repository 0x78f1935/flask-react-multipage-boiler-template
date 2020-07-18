import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Card, Button, Nav} from 'react-bootstrap';
import GithubLogo from './github.png';
import QRDonate from './donate.png';


export default class AboutPage extends React.Component {
    render () {
        return (
            <Container style={{ marginTop: '15px'}}>
                <Card className="text-center">
                    <Card.Header>Show some love!</Card.Header>
                    <Card.Link href="https://github.com/0x78f1935/" target="_blank">
                        <Card.Img variant="top" src={GithubLogo} style={{ width: '18rem', marginTop: '15px' }} className="rounded mx-auto d-block"/>
                    </Card.Link>
                    <Card.Body>
                        <Card.Title>Multi Page Flask React Boiler Template</Card.Title>
                        <Card.Text>
                            To show some love you can leave a star on GitHub or consider a donation.<br/>
                            Every donation will be put into demo servers and software development.
                        </Card.Text>
                        <Card.Link href="https://github.com/0x78f1935/flask-react-multipage-boiler-template" target="_blank">To GitHub</Card.Link>
                        <Card.Link href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5EPLY5V9PKH7Y&source=url" target="_blank">Donate</Card.Link>
                        <Card.Img variant="top" src={QRDonate} style={{ width: '9rem', margin: '15px' }} className="rounded mx-auto d-block"/>
                        <Card.Text>
                            BTC<br/>1NDqw57nWNTCKWf6VBG1uRPnqKMESUPki8
                        </Card.Text>
                    </Card.Body>
                    <Card.Footer className="text-muted">Thank you for your continued support!</Card.Footer>
                </Card>
            </Container>
        );
    } 
}