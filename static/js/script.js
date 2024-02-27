// code adapted from kudvenkat
//alert to login if trying to book
$(document).ready(function(){
    $('.btn.btn-primary').click(function(){
        $('#myAlert').show('fade');
    })

    $('#linkClose').click(function(){
        $('#myAlert').hide('fade');

    })

})
