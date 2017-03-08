import React, { PropTypes } from 'react';

class GridSection extends React.PureComponent {
  constructor(props) {
    super(props);
    this.fecthASCII = this.fecthASCII.bind(this);
  }
  fecthASCII() {
    return "ASCII";
  }
  render() {
    return (
      <div className="index"> </div>
    );
  }
}

GridSection.defaultProps = {};
GridSection.propTypes = {
};
export default GridSection;
