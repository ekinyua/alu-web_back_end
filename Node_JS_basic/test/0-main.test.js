const sinon = require('sinon');
const displayMessage = require('../0-console');
const assert = require('assert');

describe('0-main.js', () => {
  it('should display the message "Hello NodeJS!"', () => {
    // Create a spy to capture console.log output
    const consoleSpy = sinon.spy(console, 'log');

    // Call the function
    displayMessage('Hello NodeJS!');

    // Assert that console.log was called with the correct message
    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWithExactly(consoleSpy, 'Hello NodeJS!');

    // Restore the original console.log function
    consoleSpy.restore();
  });
});
