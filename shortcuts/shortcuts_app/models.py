"""Shared data classes and shortcut registry."""

from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class ShortcutLink:
    """A single launchable shortcut (name + url/value)."""
    name: str
    url: str


@dataclass
class ShortcutGroup:
    """A named group of shortcuts (can contain links or nested groups)."""
    name: str
    children: List[Union[ShortcutLink, "ShortcutGroup"]] = field(default_factory=list)


def _parse_entry(raw) -> Union[ShortcutLink, ShortcutGroup]:
    """Convert the legacy list/tuple format into ShortcutLink or ShortcutGroup."""
    if isinstance(raw, tuple):
        return ShortcutLink(name=raw[0], url=raw[1])
    if isinstance(raw, list):
        group_name = raw[0]
        children = [_parse_entry(child) for child in raw[1:]]
        return ShortcutGroup(name=group_name, children=children)
    raise ValueError(f"Unknown shortcut entry format: {raw}")


def is_group(entry) -> bool:
    return isinstance(entry, ShortcutGroup)


# ---------------------------------------------------------------------------
# Active shortcut registry
# ---------------------------------------------------------------------------

_RAW_SHORTCUT_LIST = [
    ["Work",
        ('A to Z', 'https://atoz.amazon.work/home'),
        ('Room Booking', 'https://meetings.amazon.com/#/'),
        ('Amazon Wiki', 'https://wiki.amazon.com/bin/view/Main/'),
        ('Quip Home', 'https://quip-amazon.com/browse'),
        ('Claim Commuter Benefits', 'https://myaccount.edenredbenefits.com/dashboard/home'),
        ('Embark', 'https://embark.talent.a2z.com/plans/launch-1036771'),
        ('Lyft Ride', 'https://amazon-subsidiary.luum.com/accounts/ridehome'),
        ('Coupa', 'https://amazon.coupahost.com/user/home'),
        ('AR Coupa', 'https://amazonrobotics.coupahost.com/user/home'),
    ],
    ["Purdue",
        ("myPurdue", 'https://wl.mypurdue.purdue.edu/'),
        ("Outlook", 'https://outlook.office.com/mail/'),
        ('Scheduling Assitant', 'https://timetable.mypurdue.purdue.edu/Timetabling/gwt.jsp?page=sectioning'),
        ("Push Portal", 'https://www.purdue.edu/push/patient-portal.php'),
    ],
    ["Research",
        ("The Dirty Details", "https://docs.google.com/spreadsheets/d/1-JYW60MK-SEji_e3Jdd7cxQXFn1tAniPV7Mmif07ZwI/edit?gid=0#gid=0"),
        ("Glibreth Dashboard", "https://gateway.gilbreth.rcac.purdue.edu/"),
        ("Gilbreth Usage", "https://www.rcac.purdue.edu/knowledge/gilbreth"),
    ],
    ('OverLeaf', 'https://www.overleaf.com/project'),
    ["Passwords",
        ("PWD:common", "PASSWORD_COMMON"),
        ("PWD:VPN", "PASSWORD_VPN")
    ],
]

SHORTCUT_REGISTRY: List[Union[ShortcutLink, ShortcutGroup]] = [
    _parse_entry(e) for e in _RAW_SHORTCUT_LIST
]


# ===========================================================================
# ========================== GRAVEYARD ======================================
# ===========================================================================
# Commented-out shortcuts preserved for reference / future re-activation.
# To re-enable, move entries back into _RAW_SHORTCUT_LIST above.
#
# ["Academics",
#     ["ECE 608",
#         ("BrightSpace", 'https://purdue.brightspace.com/d2l/home/1361050'),
#         ("Discussion", 'https://piazza.com/class/mednscy22lt2ce'),
#         ("Drive", 'https://drive.google.com/drive/folders/1VYHjpSXFMVDur7XEUp0To15-ErAsMFoo?usp=drive_link'),
#         ("Gradescope", "https://www.gradescope.com/courses/1093119"),
#     ],
#     ["ECE 461",
#         ("BrightSpace", 'https://purdue.brightspace.com/d2l/home/1360878'),
#         ("Discussion", 'https://piazza.com/purdue/fall2025/ece30861'),
#         ("Drive Students", 'https://drive.google.com/drive/folders/17xqM8oqQ5iKu3ZawsQH77ggTy-tREi6b'),
#         ("Gradescope", "https://www.gradescope.com/courses/1092438"),
#         ("Autograder Server", "http://dl-berlin.ecn.purdue.edu"),
#         ("TA Zoom Meeting", "https://purdue-edu.zoom.us/j/8720262746"),
#         ("Team signup sheet", "https://docs.google.com/spreadsheets/d/1uwEMKLyfXoBK0__5uJB3DNlvc_VU6_ZQJ0XThxax-rI/edit?usp=sharing"),
#         ("Drive Staff", "https://drive.google.com/drive/folders/1EpCQG1bkAblFPESTUcOF2klQSl62crVa?usp=drive_link"),
#         ("Prev Onedrive", 'https://purdue0-my.sharepoint.com/:f:/g/personal/davisjam_purdue_edu/EgqgWBmDKn9Ol6AI-6XPmUcBqTYAZIc2DcudUrZ1q7aNiw'),
#     ],
#     ["ECE 694",
#         ("BrightSpace", 'https://purdue.brightspace.com/d2l/home/1361311'),
#     ]
# ],
#
# ('Drivetrain', 'https://%s.drivetrain.ai/'),
#
# ["Github",
#     ('Netra Explainability', 'https://github.com/udaan-com/udaan-netra-explainability'),
#     ('Robosub Github', 'https://github.com/auv-iitb/robosub'),
#     ('Hello Github', 'https://github.com/Parth1811/hello'),
# ],
#
# ["Gmail",
#     ('Gmail-parthvin', 'https://mail.google.com/mail/u/0/#inbox'),
#     ('Gmail-parthpatil-udaan', 'https://mail.google.com/mail/u/1/#inbox'),
#     # ('Gmail-django.parth', 'https://mail.google.com/mail/u/3/#inbox'),
# ],
#
# ('Calendar', 'https://calendar.google.com/calendar/u/1/r?hl=en-GB&pli=1'),
# ('Placement Portal', 'https://campus.placements.iitb.ac.in/'),
# ('Placement Blog', 'http://placements.iitb.ac.in/blog/'),
# ("USCIS API", "https://my.uscis.gov/account/case-service/api/cases/IOE9321565277"),
#
# ["Discussion Groups",
#     ('AUV Software', 'https://groups.google.com/forum/#!forum/software_auv'),
#     # ('SNARE slack', 'https://app.slack.com/client/T3U3LQR6Y/C4CEKSG9E/thread/C3U3LQX7E-1582274203.072500'),
#     # ('Django IRC', 'http://webchat.freenode.net?nick=Parth1811&channels=%23django&prompt=1'),
#     # ('Zulip IRC', "https://chat.zulip.org/#narrow/stream/95-new-members/topic/GSoC.202020"),
#     # ('Processing IRC', 'https://discourse.processing.org/c/summer-of-code')
#     # ('Gitter', 'https://gitter.im/'),
# ],
#
# ["Google Sheets",
#     ("Intern", "https://docs.google.com/spreadsheets/d/1gtHfQ5kkoTUma-_VejWQyBAvYn4Bf58Q75eeaPUa--Q/edit?gid=1713903924#gid=1713903924"),
#     ("CBMC Sheet", "https://docs.google.com/spreadsheets/d/161X1THr_XqXr7HQ3FnKfecgxQCyI0aZVlrxQMHTzdoY/edit?gid=0#gid=0"),
#     ("461 Handoff", "https://docs.google.com/spreadsheets/d/1T_908snvNCGikO8o4qFtUT7QTz9usmmh0pCtogHVbYE/edit?gid=0#gid=0"),
# ],
#
# ('JioSaavn', 'https://www.jiosaavn.com/'),
# ('Workflowy', 'https://workflowy.com/'),
# ('WakaTime', 'https://wakatime.com/dashboard'),
# ('Django tickets', 'https://code.djangoproject.com/ticket/%s'),
# ('SNARE Issues', 'https://github.com/mushorg/snare/issues/'),
# ('TANNER Issues', 'https://github.com/mushorg/tanner/issues/'),
# ('VISA', 'https://cgifederal.secure.force.com/ApplicantHome'),
# ('Flex Desk Booking', 'https://indoorfinders.robotics.a2z.com/UserSite/WIO/VisualRegistration.aspx?rand=iewdpsvohy'),
#
# ["Macros",
#     ("Macro:\\begin{bmatrix} \\end{bmatrix}", r"\\begin{bmatrix} \\end{bmatrix}"),
#     ("Macro:C++ template",\
# r'''
# #include <bits/stdc++.h>
# using namespace std;
#
# #define fo(i, n) for (i = 0; i < n; i++)
# #define Fo(i, k, n) for (i = k; k < n ? i < n : i > n; k < n ? i += 1 : i -= 1)
# #define ll long long
# #define deb(x) cout << #x << "=" << x << endl
# #define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
# #define pb push_back
# #define all(x) x.begin(), x.end()
# #define clr(x) memset(x, 0, sizeof(x))
# typedef vector<int> vi;
# typedef vector<ll> vl;
# '''),
# ],
