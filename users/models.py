from django.db import models
from django.contrib.auth.models import User
from PIL import Image

ROLE = (
    # In-system value - Show value
    ('student', "STUDENT"),
    ('teacher', "TEACHER")
)

CODE_HIGHLIGHT = (
    ('a11y-dark', 'A11Y Dark'),
    ('a11y-light', 'A11Y Light'),
    ('agate', 'Agate'),
    ('an-old-hope', 'An Old Hope'),
    ('androidstudio', 'Android Studio'),
    ('arduino-light', 'Arduino Light'),
    ('arta', 'Arta'),
    ('ascetic', 'Ascetic'),
    ('atom-one-dark-reasonable', 'Atom One Dark Reasonable'),
    ('atom-one-dark', 'Atom One Dark'),
    ('atom-one-light', 'Atom One Light'),
    ('brown-paper', 'Brown Paper'),
    ('codepen-embed', 'Codepen Embed'),
    ('color-brewer', 'Color Brewer'),
    ('dark', 'Dark'),
    ('default', 'Default'),
    ('devibeans', 'Devibeans'),
    ('docco', "Docco"),
    ('far', "Far"),
    ('foundation', "Foundation"),
    ('github-dark-dimmed', 'GitHub Dark Dimmed'),
    ('github-dark', 'GitHub Dark'),
    ('github', 'GitHub'),
    ('gml', 'GML'),
    ('googlecode', 'Google Code'),
    ('gradient-dark', 'Gradient Dark'),
    ('gradient-light', 'Gradient Light'),
    ('grayscale', 'Grayscale'),
    ('hybrid', "Hybrid"),
    ('idea', "Idea"),
    ('ir-black', "IR Black"),
    ('isbl-editor-dark', 'ISBL Editor Dark'),
    ('isbl-editor-light', 'ISBL Editor Light'),
    ('kimbie-dark', 'Kimbie Dark'),
    ('kimbie-light', 'Kimbie Light'),
    ('lightfair', 'Lightfair'),
    ('lioshi', 'Lioshi'),
    ('magula', 'Magula'),
    ('mono-blue', 'Mono Blue'),
    ('monokai-sublime', 'Monokai Sublime'),
    ('monokai', 'Monokai'),
    ('night-owl', 'Night Owl'),
    ('nnfx-dark', 'NNFX Dark'),
    ('nnfx-light', 'NNFX Light'),
    ('nord', 'Nord'),
    ('obsidian', 'Obsidian'),
    ('paraiso-dark', 'Paraiso Dark'),
    ('paraiso-light', 'Paraiso Light'),
    ('pojoaque', 'Pojoaque'),
    ('purebasic', 'Pure Basic'),
    ('qtcreator-dark', 'QTCreator Dark'),
    ('qtcreator-light', 'QTCreator Light'),
    ('rainbow', 'Rainbow'),
    ('routeros', 'Routeros'),
    ('school-book', 'School Book'),
    ('shades-of-purple', 'Shades of Purple'),
    ('srcery', 'Srcery'),
    ('stackoverflow-dark', 'Stackoverflow Dark'),
    ('stackoverflow-light', 'Stackoverflow Light'),
    ('sunburst', 'Sunburst'),
    ('tomorrow-night-blue', 'Tomorrow Night Blue'),
    ('tomorrow-night-bright', 'Tomorrow Night Bright'),
    ('vs', 'Visual Code'),
    ('vs2015', 'Visual Code 2015'),
    ('xcode', 'XCode'),
    ('xt256', 'XT256'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(default='6000000000')
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    role = models.CharField(max_length=10, choices=ROLE, default='student', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# TODO: Make auto resize picture system

# class UserConfig(models.Model):
