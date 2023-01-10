import '../style/homeNavbar.css';

const NavBar = () => {


    return ( 
        <header className = "header">

            <h1 className="header-name">NE1-FREELANCE</h1>
            <nav className= "navBar">
                <ul>
                    <li>Home</li>
                    <li>Browse Jobs</li>
                    <li>Services</li>
                    <li>Blogs</li>
                    <li>About</li>
                    <li>Pages</li>
                    <li>Contact</li>
                    <li className="dashboard">Dash Board</li>
                </ul>
            </nav>
        </header>
    );
}

export default NavBar;