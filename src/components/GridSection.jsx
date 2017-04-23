import React from 'react';
// import _ from 'lodash';
// import getURL from '../utils/fetch';
/**
 * Pants module.
 * @module my/pants
 * @see module:my/shirt
 */

class GridSection extends React.PureComponent {
  constructor(props) {
    super(props);
    // this.fetchASCII = this.fetchASCII.bind(this);
    this.state = {
      asciiList: [],
    };
  }
  componentWillMount() {
    this.fetchASCII();
    console.log(this.state.asciiList);
  }
  // fetchASCII() {
  //   this.getURL('/api').then(
  //     function (data) {
  //       console.log(data, this);
  //       return data;
  //       this.setState({
  //         asciiList: data,
  //       });
  //     },
  //   );
  // }
  render() {
    return (
      <div />
    );
  }
}

export default GridSection;
