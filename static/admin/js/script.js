/**
 * @jest-environment jsdom
 */

let menu = {
    pizzas: $('#pills-pizzas .menu-item img'),
    dips: $('#pills-dips .menu-item img'),
    drinks: $('#pills-drinks .menu-item img'),
};

//make jquery functions available after the document has loaded
$(document).ready(function () {
    menu.pizzas.after('<p id="priceTag" class="float-right t-1"><strong>€14</strong></p>'); //prices under all pizza items
    menu.dips.after('<p id="priceTag" class="float-right t-1"><strong>€2</strong></p>'); //prices under all dips
    menu.drinks.after('<p id="priceTag" class="float-right t-1"><strong>€2</strong></p>'); //prices under all dips
});

