from tasks import long_add
import time

def main():
    result = long_add.delay(10,1)
    # Task should not be complete...
    print "task finished? ", result.ready()
    print "taks result: ", result.result    

    time.sleep(10)

    # Task should be complete 
    print "task finished? ", result.ready()
    print "taks result: ", result.result    

    print "DONE"

if __name__ == '__main__':
    main()