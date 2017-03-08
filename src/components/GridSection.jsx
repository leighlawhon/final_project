import React from 'react';
import _ from 'lodash';
import fetch from '../utils/fetch';

class GridSection extends React.PureComponent {
  // constructor(props) {
  //   super(props);
  //   this.fecthASCII = this.fecthASCII.bind(this);
  // }
  static fecthASCII() {
    const asciiProducts = fetch.getURL('/api');
    // console.log(this);
    return _.each(asciiProducts, product => <li>{product.face}</li>);
  }
  render() {
    return (
      <ul className="productList">
        this.fecthASCII();
      </ul>
    );
  }
}

export default GridSection;
