#!/usr/bin/env python
import requests
import json
import time
import turtle


def main():
    # part a. list of the astronauts who are currently in space
    api_url = 'http://api.open-notify.org/astros.json'
    response_url = requests.get(api_url).text
    response_url = json.loads(response_url)
    print(json.dumps(response_url, indent=4))
    print('Astronauts currently in space: ', response_url['number'])

    for info in response_url['people']:
        print('{}, is on {}'.format(
            info['name'], info['craft']))

    # part b. current geographic coordinates (lat/lon) of the space
    # station, along with a timestamp
    coord_url = requests.get('http://api.open-notify.org/iss-now.json')
    result = coord_url.json()

    coord_dict = result['iss_position']
    lat = float(coord_dict['latitude'])
    long = float(coord_dict['longitude'])
    ts = time.ctime(result['timestamp'])
    print('ISS location:lat={}, long={}, time={}'.format(lat, long, ts))

    # part d. Find next time that the ISS will be overhead Indianapolis, IN
    i = requests.get(
        'http://api.open-notify.org/iss-pass.json?lat=39.7684&lon=-86.1581')
    pass_over = i.text
    pass_over = json.loads(pass_over)
    print(pass_over)
    result_ind = pass_over['response'][0]
    next_pass = time.ctime(result_ind['risetime'])
    print("The ISS will pass over Indy: {}".format(next_pass))

    # part c. create a graphics screen with the world map background image
    screen = turtle.Screen()
    screen.setup(720, 360)
    # positive to right negative to left
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(long, lat)
    ind_dot = turtle.Turtle()
    ind_dot.shape('circle')
    ind_dot.color('yellow')
    ind_dot.penup()
    # indiana coordinates
    ind_dot.goto(-86.1581, 39.7684)
    ind_dot.write(next_pass)
    screen.exitonclick()


if __name__ == '__main__':
    main()
