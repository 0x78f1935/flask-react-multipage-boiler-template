import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar, Nav, NavDropdown, Form, FormControl, Button} from 'react-bootstrap';


export default class NavbarComponent extends React.Component {
    render () {
        return (
          <Navbar bg="light" expand="lg">
            <Navbar.Brand href="/">Boiler-Template</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="mr-auto">
                <Nav.Link href="/">Home</Nav.Link>
                <Nav.Link href="/about">About</Nav.Link>
                <NavDropdown title="Placeholder" id="basic-nav-dropdown">
                  <NavDropdown.Item href="#action/3.1">Placeholder1</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.2">Placeholder2</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.3">Placeholder3</NavDropdown.Item>
                  <NavDropdown.Divider />
                  <NavDropdown.Item href="#action/3.4">Placeholder4</NavDropdown.Item>
                </NavDropdown>
              </Nav>
              <Form inline>
                <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                <Button variant="outline-success">Search</Button>
              </Form>
            </Navbar.Collapse>
          </Navbar>
        );
    } 
}