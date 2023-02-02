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
});
