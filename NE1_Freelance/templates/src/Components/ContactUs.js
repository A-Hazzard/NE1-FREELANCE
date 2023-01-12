import '../style/contact.css';
import './Home';
import HomeNavBar from './HomeNavBar';
function ContactUs(){
    const title = 'Contact Us'
    return(
        <div className="contact">
            <HomeNavBar/>
            <div className="content">
                <h1>{ title }</h1>
                </div>
        </div>
    );
}
export default ContactUs;