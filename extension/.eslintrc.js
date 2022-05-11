module.exports = {
  extends: [
    // add more generic rulesets here, such as:
    'eslint:recommended',
    // 'plugin:vue/recommended', // Use this if you are using Vue.js 2.x.
    // 'plugin:vue/essential',
    // 'plugin:vue/strongly-recommended',
  ],
  rules: {
    // override/add rules settings here, such as:
    // 'vue/no-unused-vars': 'error'
    "consistent-return": 2,
    "indent"           : ["error", 2],
    "no-else-return"   : 1,
    "semi"             : [0, "always"],
    "space-unary-ops"  : 2,
    'arrow-parens': ['error', 'as-needed'],
    'end-of-line': ['crlf'],
    'tabWith': [2],
    'quotes': ['single', 'always'],
    'printWidth': 120,
    'no-console': 0,
    'vue/html-self-closing': ['error', {
      html: {
        void: 'always',
        normal: 'always',
        component: 'always'
      },
      svg: 'always',
      math: 'always'
    }],
  }
};