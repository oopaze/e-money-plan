from ....common.utils.repository import Repository
from ....entities import Profile


class ProfileRepository(Repository):
    def check_email_is_unique(self, email, id=0):
        print(email, id)
        user_with_email_passed = self.filter_all(
            (self.entity.email == email) & (self.entity.id != id)
        )
        return not any(user_with_email_passed)


profile_repository = ProfileRepository(Profile)
