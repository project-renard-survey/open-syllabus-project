

import $ from 'jquery';


import {
  REQUEST_RESULTS,
  RECEIVE_RESULTS,
} from '../constants';


/**
 * Query for results.
 *
 * @param {Object} params
 */
export function loadResults(params) {
  return function(dispatch) {

    // Notify start.
    dispatch(requestResults());

    $.getJSON('/api/ranks', params, function(json) {
      dispatch(receiveResults(json));
    });

  };
}


/**
 * When results are requested.
 */
function requestResults() {
  return {
    type: REQUEST_RESULTS,
  };
}


/**
 * When results are loaded.
 *
 * @param {Object} json
 */
function receiveResults(results) {
  console.log(results);
  return {
    type: RECEIVE_RESULTS,
    results,
  };
}
