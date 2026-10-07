// Last updated: 10/7/2026, 2:47:40 PM
function createHelloWorld() {
    return function(...args): string {
        return "Hello World"
    };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */