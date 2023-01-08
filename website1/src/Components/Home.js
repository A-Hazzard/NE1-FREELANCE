import '../style/home.css';
import $ from 'jquery';
import HomeNavBar from './HomeNavBar';
import bubbles from '../media/bubbles.png'
import backgroundImg from '../media/backgroundImg.png';


const Home = () => {
        // Add an event listener for the change event
        $("selectJob").on('change', function() {
        // Get the selected option
        var selectedOption = this.options[this.selectedIndex];

        // Remove the selected attribute from all options
        for (var i = 0; i < this.options.length; i++) {
            this.options[i].removeAttribute('selected');
        }

        // Add the selected attribute to the selected option
        selectedOption.attr('selected', true);
        });

    return ( 
        <div className="Home">
            <HomeNavBar/>
        <div className="frontCover">
            <img src={bubbles} alt="bubbles" className="bubbles"/>
            <img src={backgroundImg} alt="" className="backgroundImg"/>
                <div className="cta">
                    <h2 className='cta-header'>The fastest way to freelance</h2>
                    
                    <br />

                        <p className='cta-text'>Work with talented people at the most affordable price to get the most out of your time and cost</p>
                    
                    <br />

                    <div className="search-container">
                        <label htmlFor="searchJob" className="labelJobs">Search jobs</label>
                        <input type="text" name="searchJob" id="searchJob" className="userInput" placeholder="Search for..."/>
                        
                        <label htmlFor="selectJob" className="labelJobs">Select job</label>
                        <select name="selectJob" id="selectJob" className="userInput">
                            <option value="" selected>Services</option>
                            <option value="Webdesign">Web Design</option>
                            <option value="GraphicDesign">Graphic Design</option>
                            <option value="DigitalArt">Digital Art</option>
                        </select>

                        <button type="submit" className="search-btn">Search</button>
                    </div>
                </div>
            </div>
           
        </div>
    );
}

export default Home;