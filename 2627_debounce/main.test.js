const { debounce } = require('./main');

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

test('rage click is debounced', async () => {
    let counter = 0;
    const incrementer = () => counter++;
    let t = 100;
    let debouced_log = debounce(incrementer, t);
    // Simulate rage clicking: 100 clicks in a row, one each 1/t ms
    for (let i = 0; i < 100; i++) {
        debouced_log();
        await sleep(10);
    }
    // After 2*t ms, the last click should have been 
    // debounced, so counter should be 1 and not more
    await sleep(2 * t);
    expect(counter).toBe(1);
});

