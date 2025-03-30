# Backend II
## Session 1: Fundamentals of Big O Notation in Python Performance

**Goal:**
Understand how algorithm complexity is measured with Big O notation and why it matters for performance in Python.

**Definition:**
Big O notation expresses the upper bound of an algorithm’s runtime relative to its input size. It helps you compare algorithms and identify potential bottlenecks. Use cases include analysing search, sort, or any iterative processes. In Python, knowing Big O is essential for writing efficient code when dealing with large datasets.

**Documentation Reference:**
- https://docs.python.org/3/tutorial/datastructures.html
- https://en.wikipedia.org/wiki/Big_O_notation
- https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/

**Tutorial:**

- Write a simple linear search function:
```py
    def linear_search(lst, target):
        for item in lst:
            if item == target:
                return True
        return False
```
- Explanation: This function’s runtime grows linearly with the size of the list, hence O(n).

- Comparison: Briefly discuss how a binary search (O(log n)) differs in performance.

### Exercise:

- Problem: Write a recursive function to calculate factorial and determine its time complexity.
- Steps to Solve:
    - Define the recursive factorial function.
    - Analyse how many times the function is called relative to the input.

### Challenge:

- Problem: Optimise a bubble sort algorithm so that it stops early if the list is already sorted.
> Hint: Use a flag to detect whether a swap occurred.

## Session 2: Implementing Design Patterns in Python for Robust Architecture

**Goal:**
Learn key design patterns and how to implement them in Python to build maintainable and robust applications.

**Definition:**
Design patterns are standard solutions to common software design problems. They promote reusability and cleaner code structure. Use cases include managing shared resources (Singleton), abstracting object creation (Factory), and handling events (Observer). Mastery of these patterns leads to clearer communication among developers and more scalable applications.

**Documentation Reference:**
- https://refactoring.guru/design-patterns/python
- https://www.tutorialspoint.com/python_design_patterns/index.htm
- https://realpython.com/design-patterns-python/

**Tutorial:**
- Introduction to Singleton: Explain why you might need only one instance of a class.
```py
    class Singleton:
        _instance = None
        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls)
            return cls._instance

    a = Singleton()
    b = Singleton()
    print(a is b)
```
- Explanation: Both instances refer to the same object.
- Discussion: Briefly mention other patterns (Factory, Observer) for context.

### Exercise:

- Problem: Implement the Factory pattern to create shape objects (e.g., Circle and Square).

- Steps to Solve:
    - Define an abstract Shape class.
    - Create concrete classes for Circle and Square.
    - Write a factory function to return the correct object.

### Challenge:

- Problem: Implement the Observer pattern to notify multiple observers when a subject’s state changes.
- Hint: Create a Subject class that maintains a list of observers.

## Session 3: Mastering Multi-threading in Python

**Goal:**
Learn how to run code concurrently using threads to improve performance for I/O-bound tasks.

**Definition:**
Multi-threading splits a program into multiple threads running in parallel. In Python, this is ideal for I/O-bound operations because threads share the same memory space. Use cases include network operations, file I/O, and handling multiple user requests. Despite the Global Interpreter Lock (GIL), multi-threading remains effective for many practical scenarios.

**Documentation Reference:**
- https://docs.python.org/3/library/threading.html
- https://realpython.com/intro-to-python-threading/
- https://www.tutorialspoint.com/python/python_multithreading.htm

**Tutorial:**

- Introduction: Explain the threading module.

```py
    import threading
    import time

    def print_numbers():
        for i in range(5):
            print(i)
            time.sleep(1)

    thread = threading.Thread(target=print_numbers)
    thread.start()
    thread.join()
```
- Explanation: This runs the print_numbers function in a separate thread.
- Discussion: Mention when to use threads (e.g., I/O-bound tasks).

### Exercise:

- Problem: Create two threads that print letters and numbers concurrently.
- Steps to Solve:
    - Define two functions—one for letters and one for numbers.
    - Create and start a thread for each function.

### Challenge:

- Problem: Create a multi-threaded program that downloads multiple files concurrently from given URLs.
- Hint: Use the threading module along with urllib.request.urlretrieve.


Session 4: Multi-processing in Python for Scalability

Title:
Multi-processing in Python for Scalability

Goal:
Understand how to run tasks concurrently in separate processes to boost performance in CPU-bound tasks.

Definition:
Multi-processing uses separate processes with their own memory space, bypassing the Global Interpreter Lock (GIL). This technique is ideal for CPU-intensive tasks such as heavy computations or large data processing, where parallel execution on multiple cores can lead to significant speed improvements. It is commonly used in scenarios that require isolated execution environments.

Documentation Reference:

    https://docs.python.org/3/library/multiprocessing.html

    https://realpython.com/python-multiprocessing/

    https://www.geeksforgeeks.org/multiprocessing-python-set-1/

Tutorial:
Prerequisites: Basic Python skills and familiarity with threading concepts.

    Introduction: Explain the difference between threading and multi-processing.

    Step-by-Step Example:

        Import the multiprocessing module.

        Define a simple function (e.g., compute a square).

        Create and start multiple processes.

    import multiprocessing
    import time

    def compute_square(n):
        time.sleep(1)  # Simulate a heavy computation
        print(f"Square of {n} is {n*n}")

    if __name__ == "__main__":
        numbers = [2, 3, 4, 5]
        processes = []
        for number in numbers:
            p = multiprocessing.Process(target=compute_square, args=(number,))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()

    Explanation: Each process runs independently, and joining ensures all complete before the script ends.

Exercise:

    Problem Statement:
    Create a program that concurrently computes the factorial of several numbers using multi-processing.

    Steps to Solve:

        Define a recursive factorial function.

        Spawn a process for each number in a list.

    Solution:

    import multiprocessing

    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    def compute_factorial(n):
        result = factorial(n)
        print(f"Factorial of {n} is {result}")

    if __name__ == "__main__":
        numbers = [3, 4, 5]
        processes = []
        for num in numbers:
            p = multiprocessing.Process(target=compute_factorial, args=(num,))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()

    Explanation:
    Each process calculates the factorial for a given number concurrently, reducing total computation time.

Challenge:

    Problem Statement:
    Create a multi-process program that divides a large list of numbers into sublists and computes the sum of squares for each sublist concurrently.

    Hint:
    Use the Pool class from the multiprocessing module.

    Solution:

    import multiprocessing

    def sum_of_squares(numbers):
        return sum(x * x for x in numbers)

    if __name__ == "__main__":
        data = list(range(1, 101))  # List of numbers from 1 to 100
        chunk_size = 20
        chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
        
        with multiprocessing.Pool() as pool:
            results = pool.map(sum_of_squares, chunks)
        print("Sum of squares for each chunk:", results)

    Explanation:
    The program splits the data into chunks, processes each chunk in parallel, and outputs the sum of squares for every sublist.

Session 5: Asynchronous Programming in Python with asyncio and FastAPI

Title:
Asynchronous Programming in Python with asyncio and FastAPI

Goal:
Learn to write non-blocking code using asyncio and integrate it into a FastAPI endpoint.

Definition:
Asynchronous programming allows concurrent execution of tasks without waiting for each to complete sequentially. In Python, the asyncio library provides tools to write such code, which is especially useful for I/O-bound operations like web requests or database calls. This enables scalable web services by handling multiple requests simultaneously.

Documentation Reference:

    https://docs.python.org/3/library/asyncio.html

    https://fastapi.tiangolo.com/async/

    https://realpython.com/async-io-python/

Tutorial:
Prerequisites: Python knowledge, installation of FastAPI and Uvicorn.

    Setup FastAPI:

pip install fastapi uvicorn

Step-by-Step Example:

    Create an asynchronous function using async def and await.

    Define a FastAPI endpoint that calls this async function.

    from fastapi import FastAPI
    import asyncio

    app = FastAPI()

    async def simulated_io_task():
        await asyncio.sleep(1)
        return "Data fetched!"

    @app.get("/async-data")
    async def get_data():
        result = await simulated_io_task()
        return {"message": result}

    # Run using: uvicorn filename:app --reload

    Explanation: The endpoint /async-data executes the async task without blocking other requests.

Exercise:

    Problem Statement:
    Create a FastAPI endpoint that concurrently fetches data from two simulated sources using asyncio.gather.

    Steps to Solve:

        Define two async functions that simulate data fetching.

        Use asyncio.gather to run them concurrently.

    Solution:

    from fastapi import FastAPI
    import asyncio

    app = FastAPI()

    async def fetch_source_one():
        await asyncio.sleep(1)
        return "Data from source 1"

    async def fetch_source_two():
        await asyncio.sleep(1.5)
        return "Data from source 2"

    @app.get("/combined-data")
    async def get_combined_data():
        data1, data2 = await asyncio.gather(fetch_source_one(), fetch_source_two())
        return {"source1": data1, "source2": data2}

    Explanation:
    Both functions run concurrently, and their results are returned together.

Challenge:

    Problem Statement:
    Develop an asynchronous web scraper that fetches HTML content from multiple URLs concurrently using aiohttp.

    Hint:
    Use the aiohttp library with asyncio.gather.

    Solution:

    import asyncio
    import aiohttp

    async def fetch_url(session, url):
        async with session.get(url) as response:
            return await response.text()

    async def scrape_urls(urls):
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_url(session, url) for url in urls]
            return await asyncio.gather(*tasks)

    if __name__ == "__main__":
        urls = ["https://www.example.com", "https://www.python.org"]
        html_contents = asyncio.run(scrape_urls(urls))
        for content in html_contents:
            print("Fetched content length:", len(content))

    Explanation:
    The scraper creates a session and concurrently fetches content from each URL using asyncio.gather.

Session 6: Advanced Async Patterns and Concurrency Techniques

Title:
Advanced Async Patterns and Concurrency Techniques

Goal:
Explore advanced asynchronous programming concepts to manage tasks, handle timeouts, and coordinate concurrent operations efficiently.

Definition:
Beyond basic async functions, advanced patterns include task scheduling, handling cancellations, and synchronising shared resources with locks or semaphores. These techniques help in building high-load systems and real-time data processing pipelines. They are crucial when developing scalable web applications and services that demand robust concurrency management.

Documentation Reference:

    https://docs.python.org/3/library/asyncio-task.html

    https://realpython.com/python-async-features/

    https://medium.com/@kennethreitz/async-await-in-python-3-5-7b580ca64b73

Tutorial:
Prerequisites: Understanding of basic async programming.

    Creating Tasks:

        Use asyncio.create_task to run coroutines concurrently.

import asyncio

async def task_function(name, delay):
    await asyncio.sleep(delay)
    return f"{name} completed"

async def main():
    task1 = asyncio.create_task(task_function("Task 1", 1))
    task2 = asyncio.create_task(task_function("Task 2", 2))
    results = await asyncio.gather(task1, task2)
    print(results)

asyncio.run(main())

Handling Timeouts:

    Use asyncio.wait_for to set timeouts.

    async def timeout_task():
        await asyncio.sleep(2)
        return "Completed"

    async def main_timeout():
        try:
            result = await asyncio.wait_for(timeout_task(), timeout=1)
        except asyncio.TimeoutError:
            result = "Task timed out"
        print(result)

    asyncio.run(main_timeout())

    Explanation: This demonstrates cancelling a task if it exceeds the allotted time.

Exercise:

    Problem Statement:
    Write an async function that launches several tasks with a timeout and handles cancellations gracefully.

    Steps to Solve:

        Create multiple tasks using create_task.

        Wrap them with asyncio.wait_for and handle possible timeouts.

    Solution:

    import asyncio

    async def work(task_id, delay):
        await asyncio.sleep(delay)
        return f"Task {task_id} done"

    async def main():
        tasks = [asyncio.create_task(work(i, i)) for i in range(1, 4)]
        results = []
        for task in tasks:
            try:
                result = await asyncio.wait_for(task, timeout=2)
                results.append(result)
            except asyncio.TimeoutError:
                results.append("Task timed out")
        print(results)

    asyncio.run(main())

    Explanation:
    Each task is given a timeout; tasks exceeding the timeout are caught and reported.

Challenge:

    Problem Statement:
    Implement an asynchronous rate limiter that allows only a fixed number of tasks per second.

    Hint:
    Use an asyncio semaphore to control the concurrency.

    Solution:

    import asyncio
    import time

    async def limited_task(task_id, semaphore):
        async with semaphore:
            await asyncio.sleep(0.5)  # Simulated task
            return f"Task {task_id} completed at {time.time()}"

    async def main():
        semaphore = asyncio.Semaphore(2)  # Only 2 tasks allowed concurrently
        tasks = [limited_task(i, semaphore) for i in range(1, 7)]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

    asyncio.run(main())

    Explanation:
    The semaphore restricts concurrency to 2 tasks at a time, effectively rate-limiting the operations.

Session 7: Implementing Logging Best Practices in Python

Title:
Implementing Logging Best Practices in Python

Goal:
Learn to integrate and configure logging in Python applications for effective debugging and monitoring.

Definition:
Logging captures runtime events, errors, and general application flow. Python’s built-in logging module, along with third-party libraries like loguru, provides flexibility and ease of use. It is essential for debugging, performance monitoring, and security auditing in production systems.

Documentation Reference:

    https://docs.python.org/3/library/logging.html

    https://loguru.readthedocs.io/en/stable/

    https://realpython.com/python-logging/

Tutorial:
Prerequisites: Basic Python skills.

    Basic Logging Setup:

        Configure the built-in logging module.

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='app.log')
logging.info("This is an info message")
logging.error("This is an error message")

Using loguru:

    Install and use loguru for a simpler logging experience.

    from loguru import logger

    logger.add("file.log", rotation="1 MB")
    logger.debug("Debug message")
    logger.info("Info message")
    logger.error("Error message")

    Explanation: The examples show both native and third-party logging configurations.

Exercise:

    Problem Statement:
    Create a Python script that logs messages at DEBUG, INFO, WARNING, and ERROR levels.

    Steps to Solve:

        Configure logging using the built-in module.

        Log messages at different severity levels.

    Solution:

    import logging

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(message)s')
    logging.debug("Debug: Starting script")
    logging.info("Info: Processing data")
    logging.warning("Warning: Low memory")
    logging.error("Error: An error occurred")

    Explanation:
    This script prints log messages to the console at various levels.

Challenge:

    Problem Statement:
    Enhance the logging setup to rotate log files daily and include detailed timestamps.

    Hint:
    Use TimedRotatingFileHandler from the logging.handlers module.

    Solution:

    import logging
    from logging.handlers import TimedRotatingFileHandler

    handler = TimedRotatingFileHandler("timed_app.log", when="midnight", interval=1)
    handler.suffix = "%Y-%m-%d"
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[handler])
    logging.info("Logging with timed rotation")

    Explanation:
    The configuration rotates the log file at midnight, ensuring logs are segmented by date.

Session 8: Introduction to Testing in Python with pytest

Title:
Introduction to Testing in Python with pytest

Goal:
Learn the basics of writing and running tests using pytest to improve code reliability.

Definition:
Testing ensures that code behaves as expected. pytest is a powerful testing framework that simplifies writing tests and offers rich features like fixtures and parametrization. It is used for unit testing, integration tests, and continuous integration pipelines to catch errors early in development.

Documentation Reference:

    https://docs.pytest.org/en/stable/getting-started.html

    https://realpython.com/pytest-python-testing/

    https://docs.python.org/3/library/unittest.html

Tutorial:
Prerequisites: Basic Python coding skills and installation of pytest.

    Installation:

pip install pytest

Step-by-Step Example:

    Create a simple function (e.g., addition).

# app.py
def add(a, b):
    return a + b

    Write a test for the function.

# test_app.py
from app import add

def test_add():
    assert add(2, 3) == 5

    Run tests using:

    pytest

    Explanation: The test verifies the correctness of the addition function.

Exercise:

    Problem Statement:
    Write a Python function that multiplies two numbers and create a corresponding pytest test.

    Steps to Solve:

        Define the multiplication function.

        Create a test file with assertions.

    Solution:

# app.py
def multiply(a, b):
    return a * b

    # test_app.py
    from app import multiply

    def test_multiply():
        assert multiply(3, 4) == 12

    Explanation:
    Running pytest confirms that the multiplication function returns the correct result.

Challenge:

    Problem Statement:
    Write tests for a recursive factorial function using pytest parametrization.

    Hint:
    Use the @pytest.mark.parametrize decorator.

    Solution:

# app.py
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

    # test_app.py
    import pytest
    from app import factorial

    @pytest.mark.parametrize("n,expected", [
        (1, 1),
        (3, 6),
        (5, 120)
    ])
    def test_factorial(n, expected):
        assert factorial(n) == expected

    Explanation:
    Parametrization allows testing the factorial function with multiple inputs and expected outcomes.

Session 9: Advanced Testing Strategies in Django using pytest

Title:
Advanced Testing Strategies in Django using pytest

Goal:
Explore comprehensive testing techniques in Django projects using pytest to ensure robust web application functionality.

Definition:
Advanced testing in Django involves creating tests for models, views, and API endpoints using pytest-django. This approach leverages fixtures, parametrization, and a dedicated test database. It is essential for verifying that all components of a Django application work together as expected, from data models to user interfaces.

Documentation Reference:

    https://pytest-django.readthedocs.io/en/latest/

    https://docs.djangoproject.com/en/3.2/topics/testing/overview/

    https://realpython.com/django-testing-guide/

Tutorial:
Prerequisites: A basic Django project and installation of pytest-django.

    Setup:

        Install pytest-django:

pip install pytest-django

Step-by-Step Example:

    Create a simple Django model.

# models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    Write a test to check model creation.

    # test_models.py
    import pytest
    from myapp.models import Item

    @pytest.mark.django_db
    def test_item_creation():
        item = Item.objects.create(name="Test", value=10)
        assert item.name == "Test"
        assert item.value == 10

    Explanation: The test uses the Django test database to create and verify an Item instance.

Exercise:

    Problem Statement:
    Create a Django model for a BlogPost and write pytest tests to verify its methods.

    Steps to Solve:

        Define the BlogPost model with title, content, and published date.

        Write tests for creating and retrieving BlogPosts.

    Solution:

# models.py
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    # test_models.py
    import pytest
    from myapp.models import BlogPost

    @pytest.mark.django_db
    def test_blogpost_creation():
        post = BlogPost.objects.create(title="My Post", content="Content here")
        assert post.title == "My Post"
        assert "Content" in post.content

    Explanation:
    The tests ensure that BlogPost instances are created correctly and that their fields hold the expected values.

Challenge:

    Problem Statement:
    Develop a full test suite for a Django REST API endpoint (e.g., listing BlogPosts) using pytest fixtures and parametrization.

    Hint:
    Create fixtures for BlogPost objects and test the API response structure.

    Solution:

# conftest.py
import pytest
from myapp.models import BlogPost

@pytest.fixture
def blog_posts(db):
    posts = [
        BlogPost.objects.create(title="Post 1", content="Content 1"),
        BlogPost.objects.create(title="Post 2", content="Content 2")
    ]
    return posts

    # test_api.py
    import pytest
    from rest_framework.test import APIClient

    @pytest.mark.django_db
    def test_blogpost_list(blog_posts):
        client = APIClient()
        response = client.get("/api/blogposts/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == len(blog_posts)

    Explanation:
    This test suite uses fixtures to pre-populate the database and then verifies the API endpoint returns the correct data.

Session 10: Enhancing Security in Python Applications

Title:
Enhancing Security in Python Applications

Goal:
Learn techniques to secure Python web applications against common vulnerabilities.

Definition:
Security in Python involves applying best practices to prevent attacks such as SQL injection, XSS, CSRF, and more. It includes validating user input, using secure authentication methods, and implementing proper error handling. These measures are critical in protecting sensitive data and maintaining user trust in web applications.

Documentation Reference:

    https://owasp.org/www-project-top-ten/

    https://docs.djangoproject.com/en/3.2/topics/security/

    https://fastapi.tiangolo.com/advanced/security/

Tutorial:
Prerequisites: Basic web development knowledge with Django or FastAPI.

    Step-by-Step Example:

        Discuss common vulnerabilities and secure coding practices.

        Implement a FastAPI endpoint that uses JWT for authentication.

    from fastapi import FastAPI, Depends, HTTPException
    from fastapi.security import OAuth2PasswordBearer
    from jose import JWTError, jwt

    app = FastAPI()
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    SECRET_KEY = "your-secret-key"

    def verify_token(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

    @app.get("/secure-data")
    async def secure_data(user=Depends(verify_token)):
        return {"data": "Secure Information"}

    Explanation: This endpoint only returns data when a valid JWT token is provided.

Exercise:

    Problem Statement:
    Create a FastAPI endpoint that accepts user input, sanitises it, and returns a safe response.

    Steps to Solve:

        Define an endpoint that accepts query parameters.

        Apply input validation and sanitisation.

    Solution:

    from fastapi import FastAPI, Query
    from pydantic import BaseModel, validator
    import html

    app = FastAPI()

    class UserInput(BaseModel):
        content: str

        @validator('content')
        def sanitize_content(cls, v):
            return html.escape(v)

    @app.get("/sanitize")
    async def sanitize(input: UserInput = Query(...)):
        return {"sanitized": input.content}

    Explanation:
    The validator escapes HTML characters to prevent injection attacks.

Challenge:

    Problem Statement:
    Secure a Django application by implementing comprehensive security measures: CSRF protection, secure session management, and input validation.

    Hint:
    Use Django’s built-in security middleware and forms.

    Solution:
    Provide a Django settings snippet and example view that demonstrates the use of CSRF tokens and form validation.

# settings.py (snippet)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # ...
]

    # views.py
    from django.shortcuts import render
    from django.views.decorators.csrf import csrf_protect
    from django import forms

    class SafeForm(forms.Form):
        name = forms.CharField(max_length=100)

    @csrf_protect
    def safe_view(request):
        if request.method == 'POST':
            form = SafeForm(request.POST)
            if form.is_valid():
                return render(request, 'success.html', {'name': form.cleaned_data['name']})
        else:
            form = SafeForm()
        return render(request, 'form.html', {'form': form})

    Explanation:
    Django’s middleware and forms automatically manage CSRF tokens and input validation, ensuring enhanced security.

Session 11: Building GraphQL APIs with Python

Title:
Building GraphQL APIs with Python

Goal:
Learn to design and implement a GraphQL API in Python for flexible client data queries.

Definition:
GraphQL is a query language that allows clients to request exactly the data they need. In Python, libraries like Strawberry and Graphene simplify building GraphQL APIs. Use cases include mobile and web applications that require efficient and customisable data fetching.

Documentation Reference:

    https://graphql.org/learn/

    https://graphene-python.org/

    https://strawberry.rocks/docs/

Tutorial:
Prerequisites: Basic Python and web development knowledge.

    Step-by-Step Example:

        Install Strawberry:

pip install strawberry-graphql

    Define types and resolvers.

    import strawberry
    from fastapi import FastAPI
    from strawberry.asgi import GraphQL

    @strawberry.type
    class User:
        id: int
        name: str

    @strawberry.type
    class Query:
        @strawberry.field
        def user(self, id: int) -> User:
            return User(id=id, name="John Doe")

    schema = strawberry.Schema(query=Query)
    graphql_app = GraphQL(schema)

    app = FastAPI()
    app.add_route("/graphql", graphql_app)

    Explanation: This creates a GraphQL endpoint at /graphql where clients can query for user data.

Exercise:

    Problem Statement:
    Create a simple GraphQL API that allows querying and updating a user’s name.

    Steps to Solve:

        Extend the schema to include a mutation for updating the user’s name.

    Solution:

    import strawberry

    @strawberry.type
    class Mutation:
        @strawberry.mutation
        def update_name(self, id: int, new_name: str) -> str:
            # For demo, just return the new name
            return new_name

    schema = strawberry.Schema(query=Query, mutation=Mutation)

    Explanation:
    The mutation allows clients to send a new name for a user, demonstrating GraphQL’s flexibility.

Challenge:

    Problem Statement:
    Implement a GraphQL API that supports nested queries and authenticated mutations.

    Hint:
    Integrate an authentication check in the resolver.

    Solution:

    @strawberry.type
    class Mutation:
        @strawberry.mutation
        def update_name(self, id: int, new_name: str, token: str) -> str:
            if token != "valid-token":
                raise Exception("Authentication failed")
            return new_name

    schema = strawberry.Schema(query=Query, mutation=Mutation)

    Explanation:
    The resolver checks for a valid token before processing the mutation, ensuring secure updates.

Session 12: Developing gRPC Services in Python

Title:
Developing gRPC Services in Python

Goal:
Learn to build and consume gRPC services for efficient inter-service communication.

Definition:
gRPC is a high-performance RPC framework that uses Protocol Buffers for data serialization. It facilitates fast communication between microservices. Use cases include real-time data streaming, cross-language services, and distributed systems.

Documentation Reference:

    https://grpc.io/docs/languages/python/quickstart/

    https://docs.python.org/3/library/concurrent.futures.html

    https://realpython.com/python-grpc/

Tutorial:
Prerequisites: Installation of grpcio and grpcio-tools.

    Step-by-Step Example:

        Define a simple .proto file.

        Generate Python code using grpcio-tools.

        Implement a server and client.

# In terminal, run:
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto

    Server example:

    from concurrent import futures
    import grpc
    import service_pb2
    import service_pb2_grpc

    class Greeter(service_pb2_grpc.GreeterServicer):
        def SayHello(self, request, context):
            return service_pb2.HelloReply(message=f"Hello, {request.name}!")

    def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()

    if __name__ == "__main__":
        serve()

    Explanation: The server listens for incoming requests and returns a greeting.

Exercise:

    Problem Statement:
    Build a basic gRPC service that returns a greeting message for a given name.

    Steps to Solve:

        Define the .proto file, generate code, and implement the server and client.

    Solution:
    Use the code sample above.

    Explanation:
    The service demonstrates the essential components of a gRPC service in Python.

Challenge:

    Problem Statement:
    Create a gRPC service that supports server-side streaming to send multiple messages for a single request.

    Hint:
    Modify the .proto definition to use a stream for the response.

    Solution:

    # Server-side streaming implementation (snippet)
    class StreamGreeter(service_pb2_grpc.GreeterServicer):
        def StreamHello(self, request, context):
            for i in range(3):
                yield service_pb2.HelloReply(message=f"Hello {request.name}, message {i+1}")

    # Add the streaming method to the server similarly.

    Explanation:
    The server sends multiple responses for one request, demonstrating streaming with gRPC.

Session 13: Python Web Development Best Practices with Django and FastAPI

Title:
Python Web Development Best Practices with Django and FastAPI

Goal:
Learn how to structure and optimise web applications using Django and FastAPI effectively.

Definition:
Web development best practices include clear code organisation, proper error handling, security measures, and performance optimisation. By following framework-specific guidelines and industry standards, you ensure scalable and maintainable code. This session compares Django’s monolithic approach with FastAPI’s asynchronous design, highlighting key strategies for each.

Documentation Reference:

    https://docs.djangoproject.com/en/3.2/

    https://fastapi.tiangolo.com/

    https://realpython.com/django-best-practices/

Tutorial:
Prerequisites: Basic knowledge of Django and FastAPI.

    Step-by-Step Example:

        Create a simple Django project and a FastAPI app.

        Highlight differences in project structure, middleware usage, and error handling.

# Django: views.py example
from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Hello from Django"})

    # FastAPI: main.py example
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    async def index():
        return {"message": "Hello from FastAPI"}

    Explanation: This illustrates basic endpoint creation in both frameworks.

Exercise:

    Problem Statement:
    Create a minimal Django project and a FastAPI application that serve a simple "Hello World" endpoint following best practices.

    Steps to Solve:

        Set up both projects with proper directory structure.

        Implement and test the endpoints.

    Solution:
    Provide the code snippets above as a starting point.

    Explanation:
    The exercise demonstrates clear separation of concerns and framework-specific best practices.

Challenge:

    Problem Statement:
    Refactor an existing web application to improve error handling, logging, and performance optimisation.

    Hint:
    Consider integrating middleware and asynchronous processing where possible.

    Solution:
    Provide a conceptual solution with sample code adjustments.

    Explanation:
    Explain how improved organisation and error handling contribute to a more robust application.

Session 14: Introduction to AI Agents in Python with CrewAI

Title:
Introduction to AI Agents in Python with CrewAI

Goal:
Learn the basics of building AI agents using the CrewAI framework to automate tasks and respond intelligently.

Definition:
AI agents are autonomous software components that perform tasks based on user input or environmental data. CrewAI simplifies the creation of such agents by providing pre-built modules for conversation, decision-making, and integration with external services. Use cases include chatbots, automated customer support, and data analysis assistants.

Documentation Reference:

    https://crew.ai/docs

    https://github.com/crew-ai/crewai-python

    https://en.wikipedia.org/wiki/Intelligent_agent

Tutorial:
Prerequisites: Basic Python and familiarity with REST APIs.

    Step-by-Step Example:

        Install CrewAI (follow the documentation).

        Create a simple AI agent that responds to a fixed query.

    # Example pseudocode using CrewAI
    from crewai import Agent

    agent = Agent(name="SimpleAgent")
    response = agent.respond("Hello")
    print(response)

    Explanation: This example demonstrates initializing an agent and obtaining a response.

Exercise:

    Problem Statement:
    Build a simple AI agent that returns a predefined message when given a specific input.

    Steps to Solve:

        Initialise the agent.

        Define a response logic for a specific query.

    Solution:

    from crewai import Agent

    agent = Agent(name="EchoAgent")

    def respond_to_query(query):
        if query.lower() == "hello":
            return "Hi there! How can I assist you today?"
        return "I don't understand."

    print(respond_to_query("Hello"))

    Explanation:
    The function checks the input and returns a predefined response, demonstrating a basic agent logic.

Challenge:

    Problem Statement:
    Enhance the agent to handle multiple queries with different responses based on keywords.

    Hint:
    Use conditional statements or a mapping dictionary.

    Solution:

    from crewai import Agent

    agent = Agent(name="KeywordAgent")

    responses = {
        "hello": "Hello! How can I help you?",
        "bye": "Goodbye! Have a nice day.",
        "help": "I can assist with your queries."
    }

    def respond(query):
        return responses.get(query.lower(), "Sorry, I didn't catch that.")

    print(respond("help"))

    Explanation:
    The solution uses a dictionary to map queries to responses, illustrating scalable logic for an AI agent.

Session 15: Advanced AI Agent Development with CrewAI

Title:
Advanced AI Agent Development with CrewAI

Goal:
Deepen your knowledge in AI agent development by integrating state management and external API data into CrewAI agents.

Definition:
Advanced AI agents not only respond to queries but also maintain context and learn from interactions. Integrating state management and external API calls allows agents to deliver dynamic, personalised responses. Use cases include chatbots that track user history and recommendation engines that adjust responses based on real-time data.

Documentation Reference:

    https://crew.ai/docs/advanced

    https://github.com/crew-ai/crewai-python

    https://en.wikipedia.org/wiki/Artificial_intelligence

Tutorial:
Prerequisites: Completion of Session 14 and basic API integration skills.

    Step-by-Step Example:

        Extend the basic agent to store conversation history.

    from crewai import Agent

    class StatefulAgent(Agent):
        def __init__(self, name):
            super().__init__(name)
            self.history = []

        def respond(self, query):
            self.history.append(query)
            if query.lower() == "history":
                return f"Your queries: {', '.join(self.history)}"
            return f"Echo: {query}"

    agent = StatefulAgent("StatefulAgent")
    print(agent.respond(query="query"))

Session 16: Building CI/CD Pipelines for Python Projects with GitHub Actions

Title:
Building CI/CD Pipelines for Python Projects with GitHub Actions

Goal:
Learn how to automate testing, building, and deploying your Python projects using GitHub Actions.

Definition:
CI/CD stands for Continuous Integration and Continuous Deployment. It automates testing and deployment so that every code change is verified and delivered seamlessly. In Python projects, CI/CD pipelines help run tests (using pytest), build the application, and deploy to a target environment without manual intervention. This process reduces errors and accelerates development cycles.

Documentation Reference:

    https://docs.github.com/en/actions

    https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions

    https://docs.pytest.org/en/stable/

Tutorial:
Prerequisites: A GitHub repository, basic knowledge of YAML, and pytest installed.

    Create Workflow Directory: In your repository, create a folder named .github/workflows.

    Create Workflow File: Add a file named ci.yml with the following content:

    name: CI Pipeline
    on: [push, pull_request]
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.9'
          - name: Install dependencies
            run: |
              pip install pytest
              pip install -r requirements.txt
          - name: Run tests
            run: pytest

    Commit and Push: Commit the file and push to GitHub to trigger the workflow. Explanation: This workflow checks out your code, sets up Python, installs dependencies, and runs tests using pytest.

Exercise:

    Problem Statement:
    Create a GitHub Actions workflow that tests your project on multiple Python versions.

    Steps to Solve:

        Modify the YAML file to include a matrix strategy for Python versions.

    Solution:

    name: CI Pipeline
    on: [push, pull_request]
    jobs:
      test:
        runs-on: ubuntu-latest
        strategy:
          matrix:
            python-version: [3.8, 3.9, 3.10]
        steps:
          - uses: actions/checkout@v2
          - name: Set up Python ${{ matrix.python-version }}
            uses: actions/setup-python@v2
            with:
              python-version: ${{ matrix.python-version }}
          - name: Install dependencies
            run: |
              pip install pytest
              pip install -r requirements.txt
          - name: Run tests
            run: pytest

Explanation: This workflow runs tests concurrently on Python 3.8, 3.9, and 3.10.

Challenge:

    Problem Statement:
    Extend the CI/CD pipeline to include a deployment step that runs only when code is pushed to the main branch.

    Hint:
    Use conditional steps and job dependencies.

    Solution:

    name: CI/CD Pipeline
    on:
      push:
        branches: [main]
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.9'
          - name: Install dependencies
            run: |
              pip install pytest
              pip install -r requirements.txt
          - name: Run tests
            run: pytest
      deploy:
        needs: test
        runs-on: ubuntu-latest
        if: github.ref == 'refs/heads/main'
        steps:
          - uses: actions/checkout@v2
          - name: Deploy Application
            run: echo "Deploying application..."

Explanation: The deployment job depends on the test job and only runs when changes are pushed to the main branch.
Session 17: Project Module Kickoff – Requirements and Architecture

Title:
Project Module Kickoff – Requirements and Architecture

Goal:
Begin the capstone project by defining its requirements and designing a clear, scalable architecture.

Definition:
This session sets the foundation for your project module by outlining all necessary requirements and drafting an architecture diagram. It involves listing functional (features, endpoints, integrations) and non-functional (security, scalability, maintainability) requirements. A well-defined architecture helps in visualising how components (e.g., backend APIs, AI agents, CI/CD) will interact, ensuring a logical and robust design.

Documentation Reference:

    https://www.atlassian.com/agile/project-management

    https://www.uml.org/

    https://docs.djangoproject.com/en/3.2/intro/tutorial01/

Tutorial:
Prerequisites: Basic understanding of web development and design principles.

    Define Requirements:

        List key functionalities like user authentication, data handling, and AI integration.

    Design Architecture:

        Use tools like draw.io to create an architecture diagram that shows the flow between the frontend, backend, database, and AI agent.

    Document Technologies:

        Decide on frameworks (e.g., Django or FastAPI for the backend, CrewAI for AI integration) and note them in your document. Explanation: Clear requirements and a detailed architecture ensure that everyone understands the scope and design before development begins.

Exercise:

    Problem Statement:
    Write a requirements document for your project.

    Steps to Solve:

        List functional and non-functional requirements.

    Solution:

    Functional Requirements:
    - User registration and login.
    - RESTful API endpoints for data management.
    - Integration with an AI agent for chat support.

    Non-functional Requirements:
    - Secure authentication.
    - Scalable architecture.
    - Maintainable codebase.

Explanation: This document outlines what the project will achieve and sets the stage for development.

Challenge:

    Problem Statement:
    Create a detailed architecture diagram using draw.io or any similar tool.

    Hint:
    Include all major components (backend, database, AI agent, CI/CD) and their interactions.

    Solution:
    Submit your diagram as a file or provide a link to it. Explanation: A detailed architecture diagram provides a visual guide for how the project components interact.

Session 18: Project Module Development – Backend Implementation

Title:
Project Module Development – Backend Implementation

Goal:
Develop the backend of your project by creating core API endpoints, data models, and user authentication features.

Definition:
This session focuses on building the backend using a framework such as Django or FastAPI. You will implement RESTful endpoints for data operations, set up database models, and integrate authentication. This is a crucial step to ensure your application handles data securely and efficiently.

Documentation Reference:

    https://docs.djangoproject.com/en/3.2/

    https://fastapi.tiangolo.com/

    https://www.django-rest-framework.org/

Tutorial:
Prerequisites: Completion of requirements and architecture planning from Session 17.

    Set Up the Project:

        Initialize your Django or FastAPI project.

    Create Data Models:

        Define models (e.g., User, Item) and apply migrations (for Django) or use Pydantic models (for FastAPI).

    Develop API Endpoints:

        Create endpoints for CRUD operations.

        Example (FastAPI):

        from fastapi import FastAPI
        from pydantic import BaseModel

        app = FastAPI()

        class Item(BaseModel):
            name: str
            description: str

        items = []

        @app.post("/items/")
        async def create_item(item: Item):
            items.append(item)
            return item

        @app.get("/items/")
        async def get_items():
            return items

Explanation: This example shows how to define a simple API for creating and retrieving items.

Exercise:

    Problem Statement:
    Implement a user authentication system with registration and login endpoints.

    Steps to Solve:

        Define a User model.

        Create endpoints for user registration and login.

    Solution:

    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel

    app = FastAPI()

    class User(BaseModel):
        username: str
        password: str

    users = {}

    @app.post("/register/")
    async def register(user: User):
        if user.username in users:
            raise HTTPException(status_code=400, detail="User already exists")
        users[user.username] = user.password
        return {"message": "User registered successfully"}

    @app.post("/login/")
    async def login(user: User):
        if users.get(user.username) != user.password:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"message": "Login successful"}

Explanation: This solution provides endpoints for user registration and login, ensuring that user credentials are properly validated.

Challenge:

    Problem Statement:
    Enhance the backend by adding data validation and custom error handling to all endpoints.

    Hint:
    Use Pydantic models with validators and FastAPI exception handlers.

    Solution:

    from fastapi import FastAPI, HTTPException, Request
    from fastapi.responses import JSONResponse
    from pydantic import BaseModel, Field

    app = FastAPI()

    class Product(BaseModel):
        name: str = Field(..., min_length=1)
        price: float = Field(..., gt=0)

    products = []

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    @app.post("/products/")
    async def create_product(product: Product):
        products.append(product)
        return product

Explanation: This code validates input using Pydantic and handles errors gracefully with a custom exception handler.
Session 19: Project Module Development – AI Integration and Testing

Title:
Project Module Development – AI Integration and Testing

Goal:
Integrate AI agents into your backend application using CrewAI and ensure their proper functionality with thorough testing.

Definition:
This session focuses on embedding AI capabilities into your project. By integrating AI agents (using CrewAI), you can add features like chat support or intelligent data processing. Testing these integrations with pytest ensures that AI responses are handled correctly and that any failures are managed gracefully.

Documentation Reference:

    https://crew.ai/docs

    https://github.com/crew-ai/crewai-python

    https://docs.pytest.org/en/stable/

Tutorial:
Prerequisites: A functioning backend from Session 18 and basic familiarity with CrewAI.

    Integrate the AI Agent:

from crewai import Agent

agent = Agent(name="ChatAgent")

def get_ai_response(query):
    return agent.respond(query)

Create an API Endpoint:

from fastapi import FastAPI

app = FastAPI()

@app.get("/chat/")
async def chat(query: str):
    response = get_ai_response(query)
    return {"response": response}

Write Tests:
Create a test file using pytest to verify the AI endpoint.

    # test_ai.py
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)

    def test_chat_endpoint():
        response = client.get("/chat/", params={"query": "Hello"})
        data = response.json()
        assert "response" in data

Explanation: The AI agent is integrated into the backend, and tests ensure the endpoint returns a valid response.

Exercise:

    Problem Statement:
    Write tests for the AI integration endpoint to check both normal responses and error handling.

    Steps to Solve:

        Create tests using pytest for the /chat/ endpoint.

    Solution:

    # test_ai.py
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)

    def test_chat_normal():
        response = client.get("/chat/", params={"query": "Hello"})
        data = response.json()
        assert isinstance(data["response"], str)

    def test_chat_error():
        # Simulate an error by passing a query that causes a failure (if implemented)
        response = client.get("/chat/", params={"query": ""})
        assert response.status_code in [200, 400]

Explanation: These tests validate that the AI endpoint works as expected and gracefully handles errors.

Challenge:

    Problem Statement:
    Enhance the AI integration function to include error handling that returns a fallback message if the AI agent fails.

    Hint:
    Use try/except blocks within the AI response function.

    Solution:

    from crewai import Agent
    from fastapi import HTTPException

    agent = Agent(name="ResilientAgent")

    def get_ai_response(query):
        try:
            return agent.respond(query)
        except Exception:
            return "Sorry, I couldn't process your request."

Explanation: The try/except structure ensures that the API returns a fallback response if an error occurs during AI processing.
Session 20: Project Module Development – Deployment and CI/CD Integration

Title:
Project Module Development – Deployment and CI/CD Integration

Goal:
Deploy your project using GitHub Actions and integrate it into a CI/CD pipeline to automate testing and deployment.

Definition:
Deployment is the process of making your application available for users. By integrating CI/CD pipelines, you automate testing, building, and deployment, ensuring that every change is validated and deployed seamlessly. This approach enhances reliability and speeds up release cycles while allowing quick rollbacks if needed.

Documentation Reference:

    https://docs.github.com/en/actions

    https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions

    https://fastapi.tiangolo.com/deployment/

Tutorial:
Prerequisites: A working project from Sessions 18 and 19 and a GitHub repository.

    Set Up Deployment Workflow:

        Create a file .github/workflows/deploy.yml in your repository.

    name: Deploy Project
    on:
      push:
        branches: [main]
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.9'
          - name: Install dependencies
            run: |
              pip install -r requirements.txt
              pip install pytest
          - name: Run tests
            run: pytest
      deploy:
        needs: build
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Deploy Application
            run: echo "Deploying the application..."

    Test and Monitor:

        Commit and push to trigger the workflow and observe the pipeline’s output. Explanation: This CI/CD workflow ensures your project is automatically tested and deployed upon each push to the main branch.

Exercise:

    Problem Statement:
    Modify the workflow to securely use environment variables and GitHub secrets during deployment.

    Steps to Solve:

        Update the deploy step to include environment variables.

    Solution:

    name: Deploy Project
    on:
      push:
        branches: [main]
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.9'
          - name: Install dependencies
            run: |
              pip install -r requirements.txt
              pip install pytest
          - name: Run tests
            run: pytest
      deploy:
        needs: build
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Deploy Application
            env:
              DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
            run: echo "Deploying with token $DEPLOY_TOKEN..."

Explanation: This solution demonstrates how to include environment variables and GitHub secrets to securely manage deployment credentials.

Challenge:

    Problem Statement:
    Implement a rollback mechanism in the CI/CD pipeline that triggers a rollback step if deployment fails.

    Hint:
    Use conditional job steps in GitHub Actions.

    Solution:

    name: CI/CD with Rollback
    on:
      push:
        branches: [main]
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          # Build and test steps as above...
          - name: Run tests
            run: pytest
      deploy:
        needs: build
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Deploy Application
            id: deploy_step
            run: |
              if ! echo "Deploying..."; then
                exit 1
              fi
      rollback:
        needs: deploy
        runs-on: ubuntu-latest
        if: failure()
        steps:
          - name: Rollback Application
            run: echo "Rolling back deployment..."

Explanation: The rollback job is conditioned to run only if the deploy job fails, ensuring a quick recovery from deployment issues.
Session 21: Project Module Wrap-up and Final Presentation

Title:
Project Module Wrap-up and Final Presentation

Goal:
Consolidate the project, perform final testing and documentation, and prepare to present the complete solution.

Definition:
This session focuses on reviewing all project components, finalising documentation, and creating a presentation that summarises the project’s design, implementation, and outcomes. It involves comprehensive testing, writing a project report, and preparing slides to showcase the project. This is critical for reflecting on lessons learned and for professional presentation skills.

Documentation Reference:

    https://www.atlassian.com/software/jira

    https://www.lucidchart.com/pages/uml-diagram

    https://docs.microsoft.com/en-us/azure/devops/pipelines/

Tutorial:
Prerequisites: A completed project from Sessions 18–20.

    Review the Project:

        Test all endpoints, AI integrations, and security measures.

    Document the Project:

        Write a final report that includes an introduction, architecture, implementation details, testing results, and deployment strategy.

    Prepare a Presentation:

        Create a slide deck summarising key points: design decisions, challenges, solutions, and future improvements. Explanation: A thorough wrap-up ensures that every aspect of the project is understood and effectively communicated.

Exercise:

    Problem Statement:
    Write a project report that summarises the architecture, implementation, testing, and deployment phases.

    Steps to Solve:

        Create an outline with sections: Introduction, Architecture, Implementation, Testing, Deployment, and Future Work.

    Solution:

    Project Report Outline:
    1. Introduction: Objectives and scope.
    2. Architecture: Diagram and component explanation.
    3. Implementation: Key features and code highlights.
    4. Testing: Strategies and results.
    5. Deployment: CI/CD pipeline and deployment details.
    6. Future Work: Improvements and scalability plans.

Explanation: This outline guides you in writing a comprehensive report for the project.

Challenge:

    Problem Statement:
    Prepare a final slide deck that highlights the project’s architecture, challenges, solutions, and lessons learned.

    Hint:
    Use presentation tools like PowerPoint or Google Slides and include visual diagrams.

    Solution:
    Provide your slide deck file or a link to it as the final project submission. Explanation: A well-prepared presentation communicates the project’s value and technical details clearly.

