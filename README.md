1. Clone & Setup

git clone https://github.com/kshitheshs/quiz-showdown.git
cd quiz-showdown
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Run Redis (locally)

Make sure Redis is running on localhost:6379. You can install Redis via:

    macOS: brew install redis

    Ubuntu: sudo apt install redis-server

Then start it:

redis-server

3. Run the Server

uvicorn main:app --reload

Open the API docs: http://localhost:8000/docs
