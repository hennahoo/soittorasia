#-- Import Circuit Python libraries, for Raspberry Pico
import board
import audiomp3
import audiopwmio
import pwmio
import pulseio
import time
#-- Initialize the Output pins -----------------------------------
#red = pwmio.PWMOutB(board.GP11, frequency=5000, duty_cycle=0)        # Punainen ledi PWM Transistori
#blu = pwmio.PWMOutC(board.GP12, frequency=5000, duty_cycle=0)        # Sininen  ledi PWM Transistori
#gre = pwmio.PWMOutD(board.GP13, frequency=5000, duty_cycle=0)        # Vihrea   ledi PWM Transistori
#--------------------------------------------------------- 
audio = audiopwmio.PWMAudioOut(board.GP0)                            # Kaiutin  PWM Transistori
#-----------------------------------------------------------------
#top_motor = pulseio.PWMOut(board.GP10, duty_cycle=0, frequency=440, variable_frequency=True )  # Moottori PWM Transistori
top_motor = pwmio.PWMOut(board.GP10, frequency=1 )  # Moottori PWM Transistori
#-----------------------------------------------------------------
side_motor = pwmio.PWMOut(board.GP3, frequency=20 )
side_motor.duty_cycle = 1800
time.sleep(1)
# -- Load the first MP3 music to be played at first.
decoder = audiomp3.MP3Decoder(open("winding-4.mp3", "rb"))
#---------------------------------------------------------
print("Soitetaan ensimainen mp3.")
# -- PLAY THE FIRST MP3 sound file------------------------
audio.play(decoder)
while audio.playing:
    pass
# -- -----------------------------------------------------

time.sleep(2)
side_motor.duty_cycle = 0

time.sleep(1.5)
print("Sekunnin viive.")

time.sleep(2.5)
print("2.5 sekunnin viive.")

# -- Start spinning the TOP Motor
#top_motor.duty_cycle = 65535
top_motor.duty_cycle = 1000
# --------------------------------------------------------
print("Asetetaan TOP moottorille 15500 dutycycle.")




#top_motor.duty_cycle = 0
# -- LOAD THE SECOND MP3 sound file
decoder = audiomp3.MP3Decoder(open("music-box2.mp3", "rb")) 
# --------------------------------------------------------

print("Soitetaan toinen MP3.")
# -- START PLAYING THE SECOND MP3 sound file
audio.play(decoder)
while audio.playing:
    pass
print("soitettiin mp3.")
# --------------------------------------------------------


