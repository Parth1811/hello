
class BaseTaskMeta(Type):
    # some cool meta programming stuff
    # This class will enable us to throw exception every time a new task
    # object is formed thus can help us to minimize error in competiton time

    def __new__():
        '''
        For e.g.
            TaskObject.visionName.not_found_in_vision
            raise  WARNING("Wrong vision name")
        '''

        pass

class BaseTask(metaclass=BaseTaskMeta):
    timeout = 120
    pre_req = []
    status = False
    attempts = 1
    atSuccess = None
    atFailure = None
    camera = "bottom"
    fixed_orient = True
    visionName = "fivesix_arena"
    noKalman = False

    def __init__(self):
        # do some stuff
        pass

    def action(self, mastya):
        # Hook for performing actions after the task is done
        # recieves the matsya object and can perform matsya actions,
        # map manipulation etc, some really good stuff
        pass

class MasterSlaveTask(BaseTask):
    '''
    This class provides additional functionality to easily describe a big task
    which will have many smaller task for e.g. torpedo, marker_dropper, etc

    The idea is that there will be a master task and other task will be its slaves.
    slaves will only be done if the master class was sucessful. which salves will be
    in the selecction list depends on the mission file
    '''
    pass
