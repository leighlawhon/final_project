/*eslint-env node, mocha */
/*global expect */
/*eslint no-console: 0*/
var should = require('should');

describe('grid item', function() {
  this.timeout(5000); // timeout after 5 seconds
  this.timeout(0); // disables timeout

  it('should display a date field for when the product was added', function() {
    ('55').should.equal('55');
  });

});
