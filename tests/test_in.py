import time

def test_timeout():
    # This test will sleep for 60 seconds, which exceeds the 30-second timeout.
    time.sleep(60)
    assert True