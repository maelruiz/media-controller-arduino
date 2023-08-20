import spotipy
from spotipy.oauth2 import SpotifyOAuth
import serial

# Set the serial port and baud rate according to your Arduino configuration
serial_port = 'COM10'  # Replace with the actual serial port name
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

# Set up Spotify API authentication
scope = "user-modify-playback-state user-read-currently-playing user-read-playback-state"
client_id = "#"  # Replace with your Spotify API client ID
client_secret = "#"  # Replace with your Spotify API client secret
redirect_uri = "#"  # Replace with your redirect URI
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

# Adjust the volume up
def volume_up():
    sp.volume(volume_percent=sp.current_playback()["device"]["volume_percent"] + 5)

# Adjust the volume down
def volume_down():
    sp.volume(volume_percent=sp.current_playback()["device"]["volume_percent"] - 5)

# Play or pause the media
def play_pause():
    state = sp.current_playback()
    if state and state['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()

# Go to the next track
def next_track():
    state = sp.current_playback()
    if state and state['is_playing']:
        device_id = state['device']['id']
        sp.next_track(device_id=device_id)

# Go to the previous track
def previous_track():
    state = sp.current_playback()
    if state and state['is_playing']:
        device_id = state['device']['id']
        sp.previous_track(device_id=device_id)

# Main loop
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode().strip()
        if line == "Pause":
            play_pause()
            print("Pause")
        elif line == "Next":
            next_track()
            print('Next')
        elif line == "Previous":
            previous_track()
            print('Previous')
        elif line == 'Up':
            volume_up()
        elif line == 'Down':
            volume_down()
    
    # Read potentiometer value from Arduino
    if ser.in_waiting > 0:
        value = ser.readline().decode().strip()
        if value.isdigit():
            value = int(value)
            # Map potentiometer value to volume range
            volume_percent = int((value / 1023) * 100)
            sp.volume(volume_percent=value)
            print(value)
        else:
            print(value)