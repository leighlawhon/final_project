{
  "tags": {
    "allowUnknownTags": true,
    "dictionaries": ["jsdoc","closure"]
  },
  "source": {
    "includePattern": ".+\\.js(doc|x)?$",
    "excludePattern": "(^|\\/|\\\\)_"
  },
  "plugins": ["node_modules/jsdoc-babel"],
  "babel": {
      "extensions": ["js", "es6", "jsx"],
      "presets": ["es2015"]
  },
  "opts": {
    "template": {
      "theme" : "cosmo"
    }
  }
}
