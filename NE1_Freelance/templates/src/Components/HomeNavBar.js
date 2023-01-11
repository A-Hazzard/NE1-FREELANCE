import '../style/homeNavbar.css';

const NavBar = () => {


    return ( 
        <header className = "header">

            <h1 className="header-name">NE1-FREELANCE</h1>
            <nav className= "navBar">
                <ul>
                    <li><a href = "">Home</a></li>
                    <li><a href = "">Browse</a> Jobs</li>
                    <li><a href = "">Services</a></li>
                    <li><a href = "">Blogs</a></li>
                    <li><a href = "">About</a></li>
                    <li><a href = "/create">Pages</a></li>
                    <li><a href = "">Contact</a></li>
                    <li className="dashboard">Dash Board</li>
                </ul>
            </nav>
        </header>
    );
}

export default NavBar;