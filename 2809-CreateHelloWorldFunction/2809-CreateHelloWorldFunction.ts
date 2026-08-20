// Last updated: 8/20/2026, 1:55:49 AM
function createHelloWorld() {
    return function(...args): string {
        return "Hello World"
    };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */