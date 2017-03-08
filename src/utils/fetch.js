function parseResponse(contentType, response) {
  switch (contentType) {
    case 'application/x-json-stream':
      response.json().catch((error) => { Promise.reject(new Error(`Invalid JSON: ${error.message}`)); });
      break;
    case 'text/html':
      response.text().then(html => ({
        page_type: 'generic',
        html,
      })).catch(error => Promise.reject(new Error(`HTML error: ${error.message}`)));
      break;
    default:
      Promise.reject(new Error(`Invalid content type: ${contentType}`));
  }
}

const getURL = function get(url) {
  return fetch(url).then((response) => {
    if (response.ok || response.status === 200) {
      console.log(response);
      const contentType = response.headers.get('Content-Type') || '';
      return parseResponse(contentType, response);
    }

    if (response.status === 404) {
      return Promise.reject(new Error(`Page not found: ${url}`));
    }

    return Promise.reject(new Error(`HTTP error:  ${response.status}`));
  }).catch(error => Promise.reject(new Error(`Network error: ${error.message}`)),
  );
};

export default getURL;
