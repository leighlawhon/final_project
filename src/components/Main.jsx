import React, { PropTypes } from 'react';

require('normalize.css/normalize.css');
require('../styles/App.css');

const yeomanImage = require('../images/yeoman.png');

class AppComponent extends React.PureComponent {
  render() {
    return (
      <div className="index">
        <img src={yeomanImage} alt="Yeoman renerator" />
        <div className="notice">{'Please edit'}
          <code>{this.props.url}</code>
          {'to get started!'}</div>
      </div>
    );
  }
}

AppComponent.defaultProps = {};
AppComponent.propTypes = {
  url: PropTypes.string.isRequired,
};
export default AppComponent;
