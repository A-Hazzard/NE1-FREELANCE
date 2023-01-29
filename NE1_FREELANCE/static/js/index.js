$(document).ready(function(event){


    //Submit a search query if the user presses enter
    $('.search').on('keyup', function(event){
        if(event.keyCode === 13 && $(this).val() != ''){
            $('.search_form').submit();
        }

        else if($(this).val() == ''){
            alert("Don't leave search field blank")
        }
    });

    //Hides the username and email portion of the sign up form when the page loads
    $('.form-hidden').hide("fast");

    //Displays the registration/login form when get started button is clicked and also overlays a dimmed background while disabling scroll
    $(".getStarted-btn").on('click', () => {
        $(".login-form").show("fast");
        $('.form-visible').show("fast")
        $('.overlay').toggleClass('hidden');
        $('body').css("overflow", "hidden")
    })

    //If the user clicks the overlay(anywhere besides the form), the the overflow and the form is hidden and user can scroll
    $('.overlay').on('click', () => {
        $('.overlay').toggleClass('hidden');
        $('body').css('overflow-y', 'unset')
        $('.login-form').hide("fast")
        $('.form-visible').hide("fast")
        $('.form-hidden').hide("fast")
    })

     //Checks if the email field blank to alert, if not, when the user continues, it shows the 2nd layer of the form 
    $('.continue-button').click(function(){
        // var email = $('.email').val();
        // if(email != ''){
            $('.form-hidden').show("fast");
        // } else {
            // alert("Please enter email");
        // }

    });


    $('.login-form').on('submit', function(event){
        var email = $('.email').val();
        var username = $('.username').val();
        var password = $('.password').val();

    
        credentials = [email, username, password]

            //For each credential check if they are blank, if they are redirect them to a false registration link
            for (var i = 0; i < credentials.length; i++) {

                if (credentials[i].length <= 0)   {
                    $(this).attr("action", "/registered=False/")
                }
                else $('.login-form').submit();
            }
        });
});
