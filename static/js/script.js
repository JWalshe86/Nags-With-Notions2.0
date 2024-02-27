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

$(document).ready(function(){
    $('.btn.btn-primary').click(function(){
        $('#myAlert2').show('fade');
    })

    $('#linkClose2').click(function(){
        $('#myAlert2').hide('fade');

    })

})
