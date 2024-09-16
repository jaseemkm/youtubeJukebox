import pytest
from management.commands import listener
from youtubeJukebox.models import Video


@pytest.mark.django_db
class TestVideo(object):

    link = "https://www.youtube.com/BBAyRBTfsOU"

    def test_adding_video_item(self):
        added_item = listener.add_item(self.link)
        expected_result = Video.objects.filter(videoId="BBAyRBTfsOU")
        assert added_item == expected_result

    def test_getting_id(self):
        id_get = listener.get_id(self.link)
        expected_video_id = "BBAyRBTfsOU"
        assert id_get == expected_video_id
