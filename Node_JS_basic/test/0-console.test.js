const sinon = require('sinon');
const displayMessage = require('../0-console');

describe('displayMessage', () => {
  it('should print the message to the console', () => {
    // Arrange
    const consoleSpy = sinon.spy(console, 'log');
    const message = 'Hello NodeJS!';
    
    // Act
    displayMessage(message);

    // Assert
    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWithExactly(consoleSpy, message);
    
    // Clean up
    consoleSpy.restore();
  });
});
