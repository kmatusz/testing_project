Blog app example for testing taken from https://testdriven.io/blog/modern-tdd/

To run tests from the terminal: python -m pytest tests

Test if good exception is raised: 
```
    with pytest.raises(NotFound):
        query.execute()
```

Normal tests:

```
def test_get_article_by_title():
    """
    Given the article title that is stored in the database
    WHEN the execulte method is called
    THEN the method should return article
    """

    article = Article(
            author='jane@doe.com',
            title='New Article',
            content='Super extra awesome article'
        ).save()

    query = GetArticleByTitleQuery(title = article.title)
    article_obtained = query.execute()
    assert article.title == article_obtained.title    <---- here test

```

Pydantic type checking:

```
from pydantic import BaseModel, EmailStr

class Article(BaseModel):
    author: EmailStr
    title: str
    content: str
```

Other useful things for testing:
- pylint - for checking PEP8 convetions
- static type checking - to turn on in vscode
- marshmallow - for validating external data