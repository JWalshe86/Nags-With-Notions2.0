//make jquery functions available after the document has loaded
$(document).ready(function () {
    $('#pills-pizzas .menu-item img').after('<p class="float-right t-1"><strong>€14</strong></p>'); //prices under all pizza items
    $('#pills-dips .menu-item img').after('<p class="float-right t-1"><strong>€2</strong></p>'); //prices under all dips
    $('#pills-drinks .menu-item img').after('<p class="float-right t-1"><strong>€2</strong></p>'); //prices under all dips

    $("p:nth-child(2)").css("background-color", "pink").css('padding', '5px'); //background color of prices pink & padding 5px; 
});

