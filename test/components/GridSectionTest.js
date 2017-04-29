/*eslint-env node, mocha */
/*eslint no-console: 0*/
import should from 'should';
import React from 'react';
import ReactDOM from 'react-dom';
import GridSection from '../../src/components/GridSection';
import TestUtils from 'react-addons-test-utils';
var spy = sinon.spy();

describe.only('load grid section', function() {
  beforeEach(function() {
    this.GridSectionComponent = TestUtils.renderIntoDocument(<GridSection/>);
  });
  // afterEach(() => );

  it('should load the JSON', function() {
    this.GridSectionComponent.fecthASCII().should.equal("ASCII");
  });

  xit('should alert when failing to load the JSON', function() {

  });

  xit('should preload when it has more data to load', function() {

  });

  xit('should display "end of catalog" when it does not have more data to load', function() {

  });

  xit('should run a "loading"  animation for min 1 second', function() {
  });

  xit('should display 20 items', function() {
  });

  xit('should be responsive at 1170(5up), 970(4up), and 750(2up + padding)', function() {
  });

  xit('should be followed by an ad that is random and unique', function() {
  });

});
