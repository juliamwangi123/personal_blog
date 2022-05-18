import unittest
from app.models import Blog,Comment,User

class TestBlog(unittest.TestCase):
    """
    This is the class which we will use to do tests for the Blog
    """
    def setUp(self):
        """
        This will create an instance of the User and Blog before each test case
        """
        self.new_user = User(username = "Jules")
        self.new_pitch = Blog(title = "hello", user = self.new_user)
    
    def tearDown(self):
        """
        Will delete all the info from the db
        """
        Blog.query.delete()
        User.query.delete()
        Comment.query.delete()
    
    def test_instance(self):
        """
        Will test whether the new_blog is an instance of Pitch
        """
        self.assertTrue(isinstance(self.new_blog, Blog))
   
    def test_init(self):
        """
        Will test whether the new_blog is instantiated correctly
        """
        self.assertEqual(self.new_blog.title, "hello")
        
    def test_save_pitch(self):
        """
        Will test whether the user is saved into the database
        """
        self.new_blog.save_pitch()
        blogs = Blog.query.all()
        self.assertTrue(len(blogs) > 0)

    def test_relationship_user(self):
        """
            Will test whether the blog is correctly related to the user who posted it
        """
        user=self.new_blog.user.name
        self.assertTrue(user=="Jules")

​

   
