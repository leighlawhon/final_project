/*eslint-env node, mocha */
/*eslint no-console: 0*/
'use strict';

import config from 'config';

describe('appEnvConfigTests', function () {
  it('should load app config file depending on current --env', function () {
    should(config.appEnv).be.exactly('test');
  });
});
