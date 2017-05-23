# Date calculation

The Irish lottery draw takes place twice weekly on a Wednesday and a Saturday
at 8pm. Write a function that calculates and returns the next valid draw date
based on an optional supplied date time parameter. If no supplied date is
provided, assume current date time.

### Tests

In this case I used a freezegun to mock datetime more easily so before run the tests we need install dependencies:

```sh
pip install -r requirements.txt
```

1. To run all tests:

    ```sh
    python -m unittest discover
    ```
