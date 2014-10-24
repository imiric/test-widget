# -*- coding: utf-8 -*-
import json

from django.test import TestCase, Client

from .models import Content, Tag

class WebTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # In the real world, this should be done with factories
        tags = []
        for t in ['starting', 'test']:
            tags.append(Tag.objects.create(name=t))

        c = Content.objects.create(description='Test 1', image='images/test1.jpg')
        c.tags.add(tags[0])
        c = Content.objects.create(description='Test 2', image='images/test2.jpg')
        c.tags.add(tags[0])
        c = Content.objects.create(description='Test 3', image='images/test3.jpg')
        c.tags.add(tags[1])

    def test_widget(self):
        res = self.client.get('/widget/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'images/test1.jpg')
        self.assertContains(res, 'images/test2.jpg')

    def test_images_by_tag(self):
        # No Ajax
        res = self.client.get('/images/')
        self.assertEqual(res.status_code, 400)

        res = self.client.get('/images/blah', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.content.decode('utf-8'))
        self.assertEqual(data, {'status': 'OK', 'data': []})

        res = self.client.get('/images/starting', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.content.decode('utf-8'))
        expected = {'status': 'OK', 'data': [
            'http://testserver/media/images/test1.jpg',
            'http://testserver/media/images/test2.jpg',
            ]
        }
        self.assertEqual(data, expected)

        res = self.client.get('/images/test', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.content.decode('utf-8'))
        expected = {'status': 'OK', 'data': [
            'http://testserver/media/images/test3.jpg',
            ]
        }
        self.assertEqual(data, expected)
