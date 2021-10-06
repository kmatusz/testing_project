import pytest
from blog.models import Article, NotFound
from blog.queries import ListArticlesQuery, GetArticleByIdQuery, GetArticleByTitleQuery



def test_list_articles():
    """
    GIVEN 2 articles stored in the database
    WHEN the execute method is called
    THEN it should return 2 articles
    """
    Article(
        author='jane@doe.com',
        title='New Article',
        content='Super extra awesome article'
    ).save()
    Article(
        author='jane@doe.com',
        title='Another Article',
        content='Super awesome article'
    ).save()

    query = ListArticlesQuery()

    assert len(query.execute()) == 2

def test_get_article_by_id():
    """Given one article id stored in the database
    when the execute method on this id is called 
    then it should return the article
    """

    article = Article(
        author='jane@doe.com',
        title='New Article',
        content='Super extra awesome article'
    ).save()

    query = GetArticleByIdQuery(id = article.id)
    article_obtained = query.execute()
    assert article.id == article_obtained.id


def test_get_article_by_title():
    """
    Given the article title that is stored in the database
    when the execulte method is called
    then the method should return article
    """

    article = Article(
            author='jane@doe.com',
            title='New Article',
            content='Super extra awesome article'
        ).save()

    query = GetArticleByTitleQuery(title = article.title)
    article_obtained = query.execute()
    assert article.title == article_obtained.title


def test_get_article_by_title_non_existing():
    """
    Given the article title that is NOT stored in the database
    when the execulte method is called
    then the method should return exception
    """

    article = Article(
            author='jane@doe.com',
            title='New Article',
            content='Super extra awesome article'
        ).save()

    query = GetArticleByTitleQuery(title = 'Wrong title')
    
    with pytest.raises(NotFound):
        query.execute()


