from auv_state import matsya

def run_function(function_name):
    class_obj = matsya.Matsya()
    function_obj = getattr(matsya.Matsya , function_name)
    try:
        function_obj(class_obj)
        return True
    except:
        return False

def get_battery_percent(class_obj):
    if class_obj.batteryStatus != None:
        return class_obj.batteryStatus.battery
    else:
        return False
