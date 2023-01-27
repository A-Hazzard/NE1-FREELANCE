$(document).ready(function(){

    //Hides the username and email portion of the sign up form when the page loads
    $('.form-hidden').hide("fast");

    //Submit a search query if the user presses enter
    $('.search').on('keyup', function(event){
        if(event.keyCode === 13){
            event.preventDefault();
            $('form').submit();
        }
    });

    
    //Displays the registration/login form when get started button is clicked and also overlays a dimmed background while disabling scroll
    $(".getStarted-btn").on('click', () => {
        $(".login-form").show("fast");
        $('.form-visible').show("fast")
        $('.overlay').toggleClass('hidden');
        $('body').css("overflow", "hidden")
    })

    //Checks if the email field blank to alert, if not, when the user continues, it shows the 2nd layer of the form 
    $('.continue-button').click(function(){
        var email = $('.email').val();
        if(email != ''){
            $('.form-hidden').show("fast");
        } else {
            alert("Please enter email");
        }

    });


    //Checks if username/password is blank, if not submits the form
    $('.join-button').click(function(){
        var username = $('.username').val();
        var password = $('.password').val();
        if(username != '' && password != ''){
            $('.login-form').submit();
        } else {
            alert("Please enter both username and password");
        }
    });


    //If the user clicks the overlay(anywhere besides the form), the the overflow and the form is hidden and user can scroll
    $('.overlay').on('click', () => {
        $('.overlay').toggleClass('hidden');
        $('body').css('overflow-y', 'unset')
        $('.login-form').hide("fast")
        $('.form-visible').hide("fast")
        $('.form-hidden').hide("fast")
    })
});
