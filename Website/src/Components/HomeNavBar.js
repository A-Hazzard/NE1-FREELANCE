import { Link } from 'react-router-dom'
import '../style/homeNavbar.css';


const NavBar = () => { ( 
<Router>
        
        <header className = "header">
            <h1 className="header-name">NE1-FREELANCE</h1>
            <nav className= "navBar">
                <ul>
                    <li>
                        <Link to ="/home">Home</Link></li>
                    <li>
                        <Link to ="/jobs">Browse Jobs</Link></li>
                    <li>
                        <Link to="/services">Services</Link></li>
                    <li>
                        <Link to ="/blogs">Blogs</Link></li>
                    <li>
                        <Link to ="/about">About</Link></li>
                    <li>
                        <Link to ="/pages">Pages</Link></li>
                    <li>
                        <Link to ="/contact">Contact</Link></li>
                    <li className="dashboard">Dash Board</li>
                </ul>
            </nav>
           
        </header>
        </Router>
    );
}

export default NavBar;