import 'core-js/fn/object/assign';
import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';

ReactDOM.render(<App />, document.getElementById('learningGuideApp'));
console.log(window);

SE.init({
    clientId: process.env.SE_CLIENT_ID,
    key: process.env.SE_SECRET,
    channelUrl: 'http://localhost:8000/',
    complete: function (data) {
    console.log('test', data); }
});
