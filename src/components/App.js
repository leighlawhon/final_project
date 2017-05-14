require('normalize.css/normalize.css');
require('styles/App.css');
import React from 'react';
import config from '../../config'
// import stx from 'stackexchange';
class AppComponent extends React.Component {
  componentWillMount(){
    console.log('here');
    //
    fetch('https://api.stackexchange.com/2.2/users?fromdate=1298764800&todate=1298851200&order=desc&sort=reputation&site=stackoverflow')
    .then(
      (response)=> {
      return response.json();;
    })
    .then((data) =>{
      console.log(data);
    })
  }
  render() {
    return (
      <div className="index">
        <div className="notice">Please edit <code>src/components/Main.js</code> to get started!</div>
      </div>
    );
  }
}

AppComponent.defaultProps = {
};

export default AppComponent;
