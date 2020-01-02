from django.test import override_settings

from django_webtest import WebTest

from ..forms import PostForm
from .factories import PostFactory


class PostFormTests(WebTest):
    def test_init(self):
        form = PostForm()
        expected_fields = [
            'title',
            'content',
            'slug',
        ]
        # Verify that the expected fields are part of the form.
        self.assertEqual(set(expected_fields), set(form.fields))

    @override_settings(LANGUAGE_CODE='en')
    def test_blank_data(self):
        # Empty form is expected to be invalid.
        form = PostForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'title': ["This field is required."],
            'content': ["This field is required."],
            'slug': ["This field is required."],
        })

    def test_valid_data(self):
        stub = PostFactory.stub(author=None)
        data = {
            'title': stub.title,
            'slug': stub.slug,
            'content': stub.content,
        }
        form = PostForm(data)
        self.assertTrue(form.is_valid())
        saved_post = form.save()
        for field in data:
            with self.subTest(field=field):
                self.assertEqual(getattr(saved_post, field), data[field])
        with self.subTest(field='description'):
            self.assertEqual(saved_post.description, "<p>{}</p>\n".format(stub.description))
        with self.subTest(field='body'):
            self.assertEqual(saved_post.body, "<p>{}</p>\n".format(stub.body))
