from .test_base import _Test

class TestMember(_Test):
    def test_token(self):
        member = self.api.members.get('me')
