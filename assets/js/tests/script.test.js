/**
 * @jest-environment jsdom
 */

const { menu } = require("../script");

describe("menu object contains correct keys", () => {
    test("pizzas key exists", () => {
        expect("pizzas" in menu).toBe(true);
    });
    test("dips key exists", () => {
        expect("dips" in menu).toBe(true);
    });
    test("drinks key exists", () => {
        expect("drinks" in menu).toBe(true);
    });
});



