// code adapted from Web Dev Simplified How To Build A JavaScript Password Strength Meter With Regex

const strengthMeter = document.getElementById('strength-meter');
const passwordInput = document.getElementById('id_password')
const reasonsContainer = document.getElementById('reasons');
var clicked = false;


passwordInput.addEventListener('input', updateStrengthMeter);
passwordInput.addEventListener('input', clicked1);
updateStrengthMeter()

function clicked1() {
    clicked = true;
}

function updateStrengthMeter() {
    const weaknesses = calculatePasswordStrength(passwordInput.value);
    let strength = 100;
    reasonsContainer.innerHTML = '';
    weaknesses.forEach(weakness => {
        if (weakness == null) return
        strength -= weakness.deduction;
        const messageElement = document.createElement('div');
        messageElement.innerText = weakness.message;
        reasonsContainer.appendChild(messageElement)
    });
    strengthMeter.style.setProperty('--strength', strength)
}

function calculatePasswordStrength(password) {
    // individual weaknesses passed into weakness variable
    const weaknesses = []
    weaknesses.push(lengthWeakness(password))
    weaknesses.push(lowercaseWeakness(password))
    weaknesses.push(uppercaseWeakness(password))
    weaknesses.push(numberWeakness(password))
    weaknesses.push(specialCharactersWeakness(password))
    weaknesses.push(repeatCharactersWeakness(password))

    return weaknesses
}

function lengthWeakness(password) {
    const length = password.length;

    if (length <= 5 && clicked) {
        return {
            message: 'Your password is too short',
            // deducts from password strength
            deduction: 40
        }
    }
    if (length <= 10 && clicked) {
        return {
            message: 'Your password could be longer',
            // deducts from password strength
            deduction: 15
        }
    }
}

function lowercaseWeakness(password) {
    return characterTypeWeakness(password, (/[a-z]/g), 'lowercase characters')
}

function uppercaseWeakness(password) {
    return characterTypeWeakness(password, (/[A-Z]/g), 'uppercase characters')
}

function numberWeakness(password) {
    return characterTypeWeakness(password, (/[0-9]/g), 'numbers')
}

function specialCharactersWeakness(password) {
    return characterTypeWeakness(password, (/[^0-9a-zA-Z\s]/g), 'special characters')
}

function characterTypeWeakness(password, regex, type) {
    const matches = password.match(regex) || [];
    if (matches.length === 0 && clicked) {
        return {
            message: `Your password has no ${type}`,
            deduction: 20,
        }
    }
    if (matches.length <= 2 && clicked) {
        return {
            message: `Your password could use more ${type}`,
            deduction: 5,
        }
    }
}

function repeatCharactersWeakness(password) {
    // detects 2 of the same characters in a row
    const matches = password.match(/(.)\1/g) || [];
    if (matches.length > 0 && clicked) {
        return {
            message: 'Your password has repeat characters',
            deduction: matches.length * 10,
        }
    }
}

