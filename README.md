# Q-Learner-Python
The python backend for the Q-Learner Project


## To install env:
- Make sure you have virtualenv installed on you machine
  - `python -m pip install --user virtualenv`
- Create env
  - `virtualenv <name here>`
- Active env
  - `source ml4t-venv/bin/activate`
- Install required modules
  - `python -m pip install --requirement requirements.txt`
- ✅ *Done!* ✅


## Assumptions
- You have a rabbitMQ running on port 5672
  - This could include having it running in a docker container, exposing port 5672
  - In the Rabbit directory there is Dockerfile for creating a RabbitMQ Docker container. This should work... 🤔


- Pyhon 2.7
  - The requirement.txt is responsible for listing all things your env needs. These dependencies assume Python 2.7 🐍



*Note:*
  It may be nice to have a quick way to activate this env. Try adding an alias to your .bash_profile or equivalent 
    



