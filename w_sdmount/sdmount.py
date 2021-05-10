import sys
import board
import busio
import digitalio
import adafruit_sdcard
import storage


spi = busio.SPI(board.SD_SCK, board.SD_MOSI, board.SD_MISO)
cs = digitalio.DigitalInOut(board.SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
sys.path.append('/sd')
sys.path.append('/sd/audio_files')
sys.path.append('/sd/code.py')
sys.path.append('/sd/foosball_fonts')
sys.path.append('/sd/game_modes')
sys.path.append('/sd/helpers')
sys.path.append('/sd/screens')
