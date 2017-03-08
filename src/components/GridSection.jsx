import React from 'react';
import _ from 'lodash';
import getURL from '../utils/fetch';

class GridSection extends React.PureComponent {
  constructor(props) {
    super(props);
    this.fetchASCII = this.fetchASCII.bind(this);
  }
  fetchASCII() {
    const asciiProducts = getURL('/api');
    console.log(asciiProducts, this);
    return _.each(asciiProducts, product => <li>{product.face}</li>);
  }
  render() {
    return (
      <div>{this.fetchASCII()}</div>
    );
  }
}

export default GridSection;
