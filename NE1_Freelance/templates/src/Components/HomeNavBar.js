import { Link } from 'react-router-dom';

const NavBar = () => {
    return ( 
        <header className = "header">
            <h1 className="header-name">NE1-FREELANCE</h1>
            <nav className= "navBar">
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/browse-jobs">Browse Jobs</Link></li>
                    <li><Link to="/services">Services</Link></li>
                    <li><Link to="/blogs">Blogs</Link></li>
                    <li><Link to="/about">About</Link></li>
                    <li><Link to="/create">Pages</Link></li>
                    <li><Link to="/ContactUs">Contact</Link></li>
                    <li className="dashboard">Dash Board</li>
                </ul>
            </nav>
        </header>
    );
}

export default NavBar;
