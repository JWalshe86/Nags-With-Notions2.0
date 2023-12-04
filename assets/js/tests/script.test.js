/**
 * @jest-environment jsdom
 */

const { game } = require("../script");

describe("game object contains correct keys", () => {
    test("score key exists", () => {
        expect("score" in game).toBe(true);
    })
})



