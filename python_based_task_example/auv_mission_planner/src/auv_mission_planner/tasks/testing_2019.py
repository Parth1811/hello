from .base_task import BaseTask

class home(BaseTask):

class depth_setpoint(BaseTask):
    timeout = 60
    name_of_state_task = "set_point"
    map = {"z": 100}

class plank(BaseTask):
    timeout = 100
    visionName = "plank"
    attempts = 2
    name_of_state_task = "plank"
    common_pre_req = "home"
    pre_req =   ["set_point2",  "torpedo_green", "set_point3",         "marker_uncovered_O", "marker_uncovered_O"]
    atFailure = ["torpedo_red", "surface_up",    "marker_uncovered_O", "surface_up2",        "surface_up"]

    map = [
        ["plank1",                       {"x": 1000, "y": 115, "z": 120, "rz": 45}]
        ["plank2", "set_point2",         {"x": 550, "y": 310, "z": 20, "rz": 0}],
        ["plank3",                       {"x": 1000, "y": -125, "z": 120, "rz": -45}],
        ["plank4", "set_point2",         {"x": 480, "y": -170, "z": 20, "rz": 0}],
        ["plank5", "marker_uncovered_O", getPosefrom_R_theta(r="50", theta=45)],
    ]

class torpedo(MasterSlaveTask):
    pre_req_master = [home, depth_setpoint, gate_lr]
    attempts_master = 2
    camera = "front"
    visionName = "torpedoMl"
    atSuccess = ["torpedo_heart_full", "marker_bat_center", None, None, None]
    atFailure = ["torpedo_heart_full", "marker_bat_center", None, None, None]

    name_of_state_task = ["torpedo_full", "torpedo_heart_full", "torpedo_heart", "torpedo_handle_ellipse"]
    map = [
        ["torpedo",                 "buoy_not_rot", {"x": 200, "y": -500, "z": 0}],
        ["torpedo_heart_full",      "pingerA",      {"x": 0, "y": 0, "z": 15}],
        ["torpedo_heart",           "pingerA",      {"x": 0, "y": 0, "z": 15}],
        ["torpedo_handle_ellipse",                  {"x": 0, "y": 0, "z": -60}],
        ["torpedo_shoot"]
    ]

    custom_args = [
        ["torpedo_handle_ellipse", {
            "pre_req": "torpedo_heart",
            "timeout": 90   }],
        ["torpedo_shoot", {
            "timeout": 90   }]
    ]

class pinger(BaseTask):
    timeout = 420

    def action(self, matsya):
        close_task = find_closet(matsya.currentpose, first_task, second_task)
        matsya.update_map(close_task, currentpose)
