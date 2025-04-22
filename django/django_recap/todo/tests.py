from unittest import TestCase
import pytest
from todo.models import Task

@pytest.mark.django_db
@pytest.fixture()
def get_task():
    task = Task(
        title="my task",
        description = "my description"
    )
    task.save()
    yield task
    task.delete()
    
# Create your tests here.
@pytest.mark.django_db
def test_task_creation():
    assert get_task.title == "my task"
    assert not get_task.is_done

class TaskTests(TestCase):

    
    def setUp(self):
        self.task = Task.objects.create(title="cenas", description="foo")
        return super().setUp()
    
    def tearDown(self):
        self.task.delete()
        return super().tearDown()
    
    def test_task_creation(self):
        self.assertFalse(self.task.is_done)