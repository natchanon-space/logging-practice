"""
Examples of using Python's logging facility.

Run the file in Python and observe:
Which messages are actually printed on the console or to a file?
What information is in the message?

For details, see: https://docs.python.org/3/library/logging.html
"""
import logging
import sys

def logging_test(logger):
    """Log messages using each of the standard logging levels 
       plus 1 custom log level.
    """ 
    # TODO write a log message that uses each of these log levels.
    #  Your log message should be an example of the sort of information 
    #  you would log at that level:
    #
    # debug
    # info
    # warning
    # level = logging.WARN + 5 (custom log level between WARN and ERROR)
    # error
    # critical or fatal
    logging.debug("This is a DEBUG message")
    logging.info("This is a INFO message")
    logging.warning("This is a WARNING message")
    level = logging.WARN + 5  # custom log level
    logging.log(level, "This is a LEVEL (custom log level) message")
    logging.error("This is an ERROR message")
    logging.critical("This is a CRITICAL message")


def simple_config():
    """Configure logging using basicConfig for simple configuration.

    You should call this before creating any logging objects.
    You can call basicConfig only once. 

    Some named attributes you can set using basicConfig are:

        filename = "name of a file to send log messages to"
        filemode = 'a' (append), 'w' (truncate & open for writing)
        format = a string describing format of log messages
        stream = name of a StreamHandler to use, cannot use with filename attribute
        level = the root logger level (threshold level for log msgs)

    See:  help(logging.basicConfig)
    https://docs.python.org/3/library/logging.html#logging.basicConfig
    """
    # use a custom format for log messages
    FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT)


def my_config():
    """Write your own logging configuration."""
    # TODO write your own logging configuration
    #      specify a log file, threshold level, format, and append mode
    FORMAT = '%(asctime)s %(name)s %(levelname)s(%(levelno)s): %(message)s %(lineno)d'
    logging.basicConfig(
        format=FORMAT, 
        level=0, 
        filename="logging_demo.log", 
        # filemode='w'
        )


if __name__ == "__main__":
    #
    # TODO Configure logging using one of these choices:

    # 1. Call basicConfig with the default settings
    # logging.basicConfig()

    # 2. Call simple_config to set the format of log messages.
    #    Comment out the above call (#1) to basicConfig for this.
    # simple_config()

    # 3. my_config() write your own logging configuration as
    #    described in the assignment. 
    #    Comment out the above calls to simple_config and basicConfig.
    my_config() 

    # Log some messages to the root logger using different logging levels.
    
    # root logger
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING) 
    print("Logging to ", str(logger))
    logging_test(logger)

    # TODO create a named logger, set a a custom log threshold,
    #       and call logging_test again with your named logger.
    # logging for the 'foo' module
    mylogger = logging.getLogger("foo")
    mylogger.setLevel(logging.DEBUG)  # log everything
    logging_test(mylogger)


