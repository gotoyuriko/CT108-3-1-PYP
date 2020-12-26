import json


def admin_login_read():
    with open("admin_login.txt") as adminf:
        admin_data = adminf.read()
        admin_dict = json.loads(admin_data)

    return admin_dict


def coach_read():
    with open("coach.txt") as coachf:
        coach_data = coachf.read()
        coach_list = json.loads(coach_data)

    return coach_list


def coach_write(coach_list):
    with open("coach.txt", "w") as coachf:
        encode_coach = json.dumps(coach_list)
        coachf.write(encode_coach)


def sport_center_read():
    with open("sport_center.txt") as sportcenterf:
        sportcenter_data = sportcenterf.read()
        sportcenter_list = json.loads(sportcenter_data)

    return sportcenter_list


def sport_read():
    with open("sport.txt") as sportf:
        sport_data = sportf.read()
        sport_list = json.loads(sport_data)

    return sport_list


def sport_write(sport_list):
    with open("sport.txt", "w") as sportf:
        encode_sport = json.dumps(sport_list)
        sportf.write(encode_sport)
