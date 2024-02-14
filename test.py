from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://videojs.com/advanced/?video=disneys-oceans")

driver.implicitly_wait(5)

playButton = driver.find_element(By.CLASS_NAME, "vjs-big-play-button")
playButton.click()

time.sleep(10)

videoPlayer = driver.find_element(By.ID, "preview-player")
classAttributes = videoPlayer.get_attribute('class')
classNames = classAttributes.split(' ')

assert 'vjs-playing' in classNames
assert 'vjs-has-started' in classNames
assert 'vjs-user-active' in classNames

videoPlaylist = driver.find_element(By.CLASS_NAME, "vjs-playlist-item-list")
videos = videoPlaylist.find_elements(By.TAG_NAME, "li")

nextVideoClass = "vjs-playlist-item vjs-up-next"

for video in videos[1:3]:
    text = video.get_attribute('class')
    video.click()
    assert text in nextVideoClass
    time.sleep(10)


