# django_power
Django Benchmark

# How Slow is Django anyway?
I don't really care how much more `hello world`s per second can `go lang` or `express js` can do. But I often need to know how much my `EC2 micro` + `nginx` + `gunicorn` + `django app` can handle. Or do I need second instance or `celery`? Or when both?

# Intent
I want to test different common django setups and see how much in general they can handle to have a educated guess next time. 

# Type II supernova
I want to have a standard candle of the simple CRUD django app and AWS EC2 micro instance.

* `test_server`
    1. Simple Django CRUD app
    2. URls:

# Test strategy
* deploy standard candle
* make some requests
* publish results

# TODO
* develop test_server: Django app to be tested
* develop test_client: Django app generating all the requests and storing response information

# 