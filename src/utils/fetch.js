// import _ from 'lodash';
// /** Checks Content Type and Parses accordingly.  */
// /** NOTE: I added this becasue I needed something to parse the NDJSON and
// went ahead and left the other two in there so that I could reuse this at a
// later date */
// function parseResponse(contentType, response) {
//   let parsedResults = '';
//   switch (contentType) {
//     case 'application/json':
//       parsedResults = response.json().catch((error) => {
//         Promise.reject(new Error(`Invalid JSON: ${error.message}`));
//       });
//       break;
//     case 'application/x-json-stream':
//       parsedResults = response.text()
//         .then((result) => {
//           const results = result.split('\n');
//           if (results[results.length - 1] === '') {
//             results.pop();
//           }
//           return _.map(results,
//             record => JSON.parse(record),
//           );
//         })
//         .catch(error => Promise.reject(new Error(`NPJSON error: ${error.message}`)));
//       break;
//     case 'text/html':
//       parsedResults = response.text().then(html => ({
//         page_type: 'generic',
//         html,
//       })).catch(error => Promise.reject(new Error(`HTML error: ${error.message}`)));
//       break;
//     default:
//       Promise.reject(new Error(`Invalid content type: ${contentType}`));
//   }
//   return parsedResults;
// }
//
// const getURL = function get(url) {
//   return fetch(url).then((response) => {
//     if (response.ok || response.status === 200) {
//       console.log(response);
//       const contentType = response.headers.get('Content-Type') || '';
//       const parsedResponse = parseResponse(contentType, response);
//       console.log(parsedResponse);
//       parsedResponse.then((data) => {
//         console.log(data);
//       });
//       return parsedResponse;
//     }
//
//     if (response.status === 404) {
//       return Promise.reject(new Error(`Page not found: ${url}`));
//     }
//
//     return Promise.reject(new Error(`HTTP error:  ${response.status}`));
//   }).catch(error => Promise.reject(new Error(`Network error: ${error.message}`)),
//   );
// };
//
// export default getURL;
