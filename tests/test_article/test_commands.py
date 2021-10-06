import pytest

from blog.models import Article
from blog.commands import CreateArticleCommand, AlreadyExists

def test_create_article():
    """
    Given CreateArticleCommand with valid properties
    When the execute method is called 
    Then a new article must exist in the database with the same attributes
    """

    cmd = CreateArticleCommand(
        author = 'john@doe.com',
        title = 'New title',
        content = 'Super awesome article'
    )

    article = cmd.execute()

    db_article = Article.get_by_id(article.id)

    assert db_article.id == article.id
    assert db_article.author == article.author
    assert db_article.title == article.title
    assert db_article.content == article.content


def test_create_article_already_exists():
    """
    Given CreateArticleCommand with a title already existing in the database
    When the Execute method is called
    Then the AlreadyExists exception will be raised
    """

    Article(
        author='jane@doe.com',
        title='New Article',
        content='Super extra awesome article'
    ).save()


    cmd = CreateArticleCommand(
        author='john@doe.com',
        title='New Article',
        content='Super awesome article'
    )

    with pytest.raises(AlreadyExists):
        cmd.execute()