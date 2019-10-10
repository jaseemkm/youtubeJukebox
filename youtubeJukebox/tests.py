import pytest
from management.commands import listener
from youtubeJukebox.models import Video


@pytest.mark.django_db
def test_adding_video_item():
    link = "https://www.youtube.com/BBAyRBTfsOU"
    added_item = listener.add_item(link)
    expected_result = Video.objects.filter(videoId="BBAyRBTfsOU")
    assert added_item == expected_result
