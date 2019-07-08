from number_sotrage_microservice import create_app
from number_sotrage_microservice.thread_safe_number import ThreadSafeNumber

if __name__ == '__main__':
    app = create_app(ThreadSafeNumber())
    app.run(threaded=True)
