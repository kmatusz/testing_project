from typing import List
from pydantic import BaseModel
from blog.models import Article

from pydantic import BaseModel, EmailStr, Field

class ListArticlesQuery(BaseModel):
    def execute(self) -> List[Article]:
        return Article.list()
        
class GetArticleByIdQuery(BaseModel):
    id: str

    def execute(self) -> Article:
        return Article.get_by_id(self.id)

class GetArticleByTitleQuery(BaseModel):
    title: str

    def execute(self) -> Article:
        return Article.get_by_title(title=self.title)
        