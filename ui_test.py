from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://videojs.com/advanced/?video=disneys-oceans")
driver.implicitly_wait(5)

GREEN_COLOR = "\033[92m"

def assert_video_is_playing(idx):
    time.sleep(8)
    video_player = driver.find_element(By.ID, "preview-player")
    class_attributes = video_player.get_attribute('class')
    class_names = class_attributes.split(' ')
    print(f"{GREEN_COLOR}Assertion N {idx} passed successfully!")
    assert 'vjs-playing' in class_names
    assert 'vjs-has-started' in class_names

def get_videos():
    video_playlist = driver.find_element(By.CLASS_NAME, "vjs-playlist-item-list")
    return video_playlist.find_elements(By.TAG_NAME, "li")


def get_video_title(element):
    return element.find_element(By.CLASS_NAME, "vjs-playlist-name").text

def run():
    idx = 1
    videos = get_videos()
    next_video_title = get_video_title(videos[idx])
    playlist_length = len(videos)
    
    # first video case
    video_player = driver.find_element(By.ID, "preview-player")
    video_player.click()
    assert_video_is_playing(idx)

    for video in videos[1:]:
        idx = idx + 1
        actual_video_title = get_video_title(video)
        video.click()

        assert_video_is_playing(idx)
        assert actual_video_title == next_video_title

        if idx == playlist_length - 1:
            break
        next_video_title = get_video_title(videos[idx])

run()


