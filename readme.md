# How to run the tests

To install the packages, run the following command in your terminal:

```pip install -r requirements.txt```

If an error related to permissions occurs during the installation of dependencies, use the command --user:

```pip install --user -r requirements.txt```

The first test was the UI test, where the objective was to play the first video, ensure that the video was playing, and follow the playlist, ensuring the same points in each watched video.

The first video is an atypical case, where the play action and asserts are performed outside the loop to avoid 
the verification being done in each iteration of the `for`.

To run the first test, run the following command in your terminal:

```python ui_test.py```


The second one was an API test, where we used GET methods to generate responses in JSON format and performed asserts on the request status.

When using the API, I noticed that the request statuses were always the same: 200. Therefore, I added asserts within the JSON content.

To run the second test, run the following command in your terminal:

```python api-test.py```