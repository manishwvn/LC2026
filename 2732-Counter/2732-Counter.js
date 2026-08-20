// Last updated: 8/20/2026, 1:55:51 AM
/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let curr = n - 1
    return function() {
        curr += 1
        return curr
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */