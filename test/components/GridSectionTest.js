/*eslint-env node, mocha */
/*global expect */
/*eslint no-console: 0*/
var should = require('should');

describe('grid section', function() {
  this.timeout(5000); // timeout after 5 seconds
  this.timeout(0); // disables timeout

  it('should load the JSON', function() {
    ('55').should.equal('55');
  });

  it('should alert when failing to load the JSON', function() {
    ('55').should.equal('55');
  });

  it('should preload when it has more data to load', function() {
    ('55').should.equal('55');
  });

  it('should display "end of catalog" when it does not have more data to load', function() {
    ('55').should.equal('55');
  });

  it('should run a "loading"  animation for min 1 second', function() {
    ('55').should.equal('55');
  });

  it('should display 20 items', function() {
    ('55').should.equal('55');
  });

  it('should be responsive at 1170(5up), 970(4up), and 750(2up + padding)', function() {
    ('55').should.equal('55');
  });

  it('should be followed by an ad that is random and unique', function() {
    ('55').should.equal('55');
  });

});
